import pygame

class Island():
    def __init__(self, screen, ai_settings, pos=(600,400)):
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = ai_settings.island_image
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = pos