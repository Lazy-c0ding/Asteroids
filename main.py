import sys
from asteroid import *
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print("Starting asteroids!")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
            for sh in shots:
                if sh.check_collision(asteroid):
                    asteroid.split()
        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
#end project 
