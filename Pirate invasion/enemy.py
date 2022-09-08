import math
from random import randint
import pygame
from pygame.math import Vector2

class Enemy():
            
    def __init__(self, ai_settings, screen, ship, cannonballs):
        self.screen = screen
        self.ai_settings = ai_settings
        #load the ship and get its rect.
        self.image = ai_settings.enemy_image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Randomize position of the ship
        
        self.rngx = randint(0, ai_settings.screen_width)
        self.rngy = randint(0, ai_settings.screen_height)
        self.pos = (self.rngx,self.rngy)
        
        
        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
        self.original_image = self.image
        self.rect = self.image.get_rect(center=self.pos)
        self.moving_left = False
        self.moving_right = False
        self.position = Vector2(self.pos)
        self.direction = Vector2(1,0)
        self.ship_speed = ai_settings.enemy_ship_speed
        self.accelerate = True
        self.angle = 0
        
        
        #Establish the center of the screen        
        self.x_centered = ai_settings.screen_width / 2
        self.y_centered = ai_settings.screen_height / 2
        self.angle = 270-math.atan2(self.y_centered - self.rect.centery,self.x_centered - self.rect.centerx)*180/math.pi
        
        
        #Set direction towards middle of the screen
        self.distance = [self.x_centered - self.rect.centerx, self.y_centered - self.rect.centery]
        self.norm = math.sqrt(self.distance[0] ** 2 + self.distance[1] ** 2)
        self.direction = Vector2(self.distance[0] / self.norm, self.distance[1] / self.norm)
        #Turn the image towards the middle of the screen
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def update(self):
        self.position += self.direction * self.ship_speed
        self.rect.center = self.position
        
        #print(self.angle) #debug
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)