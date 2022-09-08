import pygame
from pygame.math import Vector2
import game_functions as gf


class Cannonball():
    """A class to manage cannonball fired from the ship"""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a cannonball object at the ship's current position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Create a cannonball rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0,ai_settings.cannonball_width,ai_settings.cannonball_height)
        self.rect.center = ship.rect.center
        
        #Store the cannonball's position as a decimal value
        self.position = Vector2(self.rect.center)
           
        self.direction = ship.direction
        self.speed_factor = ai_settings.cannonball_speed_factor * self.direction
        self.speed_factor.rotate_ip(270)
        

        
        self.cannonball = ai_settings.cannonball
        self.time_alive = ai_settings.cannonball_timer * 1000
        
        self.starttime = pygame.time.get_ticks()
        self.endtime = self.starttime + self.time_alive
        
    
    def update(self, ripples):
        """move the cannonball"""
        #update the decimal position of the bullet
        self.position += self.speed_factor
        #update the rect position
        self.rect = self.position
        self.current_time = pygame.time.get_ticks()
        self.time_left =  self.endtime - self.current_time
        
        if self.time_left <= 0:
            self.list.remove(self)
            gf.ripple_event(self.screen, self.ai_settings, self.position, ripples)
            
        
        
    def timer(self, list):
        self.list = list
        
        
        #print(self.timer) #DEBUG
        
    def blitme(self):
        """draw the cannonball at its current location"""
        self.screen.blit(self.cannonball, self.rect)