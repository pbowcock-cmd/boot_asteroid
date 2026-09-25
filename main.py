from asteroidfield import AsteroidField
import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from logger import log_event
from circleshape import CircleShape
import sys

from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
#time clock
    clock=pygame.time.Clock()
    dt=0.0

 # containers
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers=(shots,drawable, updatable)

#player
    player=Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
#ASTEROID FIElD
    field=AsteroidField()



 #game loop
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for a in asteroids:
           if a.collides_with(player):
               log_event("player_hit")
               print ("Game over!")
               sys.exit()
        for a in asteroids:
            for s in shots:
                if a.collides_with(s):

                    log_event("asteroid_shot")
                    a.split()
                    s.kill()
        for o in drawable:
            o.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
     main()
