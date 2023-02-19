import pygame

class tank():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("Sprite/Tank.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mr = False
        self.ml = False
        self.mu = False
        self.md = False



    def output(self):
        self.screen.blit(self.image, self.rect)
    def update_Tanks(self):
        if self.mr and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 10
        if self.ml and self.rect.left > 0:
            self.rect.centerx -= 10
        if self.mu and self.rect.top > 0:
            self.rect.bottom -= 10
        if self.md:
            self.rect.bottom +=10





