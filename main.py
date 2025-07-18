import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from shot import *
pygame.init()
clock = pygame.time.Clock()
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    Shot.containers = (shots, updatable, drawable)

    DT = 0


    # sets framerate and draws black screen every frame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000    
        screen.fill((0,0,0))
        updatable.update(dt)
        for draws in drawable:
            draws.draw(screen)

        for asteroid in asteroids:
            if CircleShape.collision(asteroid, ship) == True:
                print("Game over!")
                sys.exit()
            for shot in shots:
                if CircleShape.collision(asteroid, shot) == True:
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
    


if __name__ == "__main__":
    main()
