import pygame
import sys
from Tanks import tank

def events(Tanks):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Tanks.mr = True
            elif event.key == pygame.K_LEFT:
                Tanks.ml = True
            elif event.key == pygame.K_UP:
                Tanks.mu = True
            elif event.key == pygame.K_DOWN:
                Tanks.md = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Tanks.mr = False
            elif event.key == pygame.K_LEFT:
                Tanks.ml = False
            elif event.key == pygame.K_UP:
                Tanks.mu = False
            elif event.key == pygame.K_DOWN:
                Tanks.md=False



