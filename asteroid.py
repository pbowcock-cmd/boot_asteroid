import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius<= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        r_a=random.uniform(20,50)
        p_angle=self.velocity.rotate(r_a)
        n_angle=self.velocity.rotate(-r_a)
        new_rad= self.radius-ASTEROID_MIN_RADIUS

        asteroid1=Asteroid(self.position.x , self.position.y ,new_rad)
        asteroid1.velocity=p_angle*1.2

        asteroid2=Asteroid(self.position.x , self.position.y ,new_rad)
        asteroid2.velocity=n_angle*1.2
