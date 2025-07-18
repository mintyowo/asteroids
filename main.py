import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
pygame.init()
clock = pygame.time.Clock()
def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Asteroid.containers = (asteroid, updatable, drawable)
    Player.containers = (updatable, drawable)
    DT = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    a = f"""
    Starting Asteroids!
    Screen width: {SCREEN_WIDTH}
    Screen height: {SCREEN_HEIGHT}
    """
    print(a)
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

        pygame.display.flip()
    


if __name__ == "__main__":
    main()
