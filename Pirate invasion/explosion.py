import pygame
import game_functions as gf

class Explosion():
    
    def __init__(self, screen, position, ai_settings):
        
        self.screen = screen
        self.position = position
        self.explosion_image = ai_settings.explosion_image.convert_alpha()
        self.counter = ai_settings.explosion_timer
        pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
        
    def update(self):
        pass
        
    def timer(self, list):
        if self.counter > 1:
            self.counter -= 1
            self.explosion_image.set_alpha(120)
        else:
            list.remove(self)
        
    def blitme(self):
        self.screen.blit(self.explosion_image, self.position)
        