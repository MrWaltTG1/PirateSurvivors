import pygame
from pygame.math import Vector2

class Island():
    def __init__(self, screen, ai_settings, pos=(600,350)):
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = ai_settings.island_image
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect(center=pos)
        self.circle_rect = pygame.draw.circle(self.screen, (255,0,0), self.rect.center, 100)
        self.rect = self.circle_rect
        print(self.rect)

    def update(self):
        pass
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)