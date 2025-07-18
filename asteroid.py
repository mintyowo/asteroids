from circleshape import *
from main import *
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        position = self.position
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ran_dum = random.uniform(20, 50)
            left_vector = self.velocity.rotate(ran_dum)
            right_vector = self.velocity.rotate(-ran_dum)
            asteroid1 = Asteroid(position, position, new_radius)
            asteroid2 = Asteroid(position, position, new_radius)
            asteroid1.velocity = left_vector * 1.2
            asteroid2.velocity = right_vector * 1.2


