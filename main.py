# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shoots, updatable, drawable)
    AsteroidField()
    player=Player(x, y)
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for bodies in drawable:
            bodies.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collition(player):
                print("Game over!")
                return
        for asteroid in asteroids:
            for shoot in shoots:
                if asteroid.collition(shoot):
                    asteroid.split()
                    shoot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
