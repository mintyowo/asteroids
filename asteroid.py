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
    def random(self):
        return random.uniform(0, 180)
    def split(self):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        position = self.position
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            left_vector = self.velocity.rotate(self.random())
            right_vector = self.velocity.rotate(-self.random())
            asteroid1 = Asteroid(position, position, new_radius)
            asteroid2 = Asteroid(position, position, new_radius)
            asteroid1.velocity = left_vector * 1.2
            asteroid2.velocity = right_vector * 1.2


    def scoreincrease(self):
        global POINTS_PER_ROCK
        global SCORE
        SCORE = SCORE + POINTS_PER_ROCK + (self.radius / 2)
        print(SCORE)
        
def gameover():
    global SCORE
    print("Game over!")
    print(f"You got {SCORE} points!")
    sys.exit()
