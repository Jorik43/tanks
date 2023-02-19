import pygame

class map():
    def __init__(self,screen):
        """карта"""


        self.screen = screen
        self.image = pygame.image.load('Sprite/Map.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def output(self):
        """рисование карты"""
        self.screen.blit(self.image, self.rect)

