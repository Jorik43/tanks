import pygame
import control
from Tanks import tank
from Map import map
def run():

    pygame.init()
    screen = pygame.display.set_mode((1920, 1000))
    pygame.display.set_caption("Танчики")
    bg = (0, 0, 0)
    Tanks = tank(screen)
    Map= map(screen)
    while True:
        control.events(Tanks)
        Tanks.update_Tanks()
        screen.fill(bg)
        Map.output()
        Tanks.output()
        pygame.display.flip()
run()




