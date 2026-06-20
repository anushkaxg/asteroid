import pygame
from logger import log_state,log_event
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids,updatable,drawable)

    AsteroidField.containers = (updatable,)

    Shot.containers = (shots,drawable,updatable)

    asteroidf = AsteroidField()

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        dt = clock.tick(60) / 1000
        # print(dt)
        for player in updatable:
            player.update(dt)
        for aster in asteroids:
            if aster.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for aster in asteroids:
            for sh in shots:
                if aster.collides_with(sh):
                    log_event("asteroid_shot")
                    aster.split()
                    sh.kill()
        screen.fill("black")
        for player in drawable:
            player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
