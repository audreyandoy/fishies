import pygame
import random
from pygame.locals import *
import sys

from fish import *

pygame.init()
screen_info = pygame.display.Info()

# set width and height of the screen
screen_size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

color = (0, 127, 255)
school = []


def main():
    for i in range(10):
        school.append(Fish((width/2, height/2)))
   
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                school.append(Fish(event.pos))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    for i in range(len(school) // 2 ):
                        school.pop(0)
        screen.fill(color)
        for x in school:
            x.update()
            x.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()