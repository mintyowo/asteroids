import pygame
from constants import *
from player import *
pygame.init()
clock = pygame.time.Clock()
def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    DT = 0 
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
        ship.update(dt)
        ship.draw(screen)
        
        pygame.display.flip()
    


if __name__ == "__main__":
    main()
