
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        old_rad = self.radius
        x = self.position.x
        y = self.position.y
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        log_event("asteroid_split")
        new_ang = random.uniform(20,50)
        ast1 = pygame.math.Vector2.rotate(self.velocity, new_ang)
        ast2 = pygame.math.Vector2.rotate(self.velocity,-new_ang)
        new_rad = old_rad - ASTEROID_MIN_RADIUS

        aster1 = Asteroid(x,y,new_rad)
        aster2 = Asteroid(x,y,new_rad)
        aster1.velocity = ast1*1.2
        aster2.velocity = ast2*1.2
