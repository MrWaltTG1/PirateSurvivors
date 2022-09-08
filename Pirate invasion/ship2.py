import pygame
from pygame.math import Vector2

class Ship():
    
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load the ship and get its rect.
        self.image = ai_settings.ship_image
        self.original_image = self.image
        self.screen_rect = screen.get_rect()
        
        
        #Load position and direction
        self.pos = ai_settings.ship_pos
        self.position = Vector2(self.pos)
        self.direction = Vector2(1,0)
        self.rect = self.image.get_rect(center=self.pos)


        #Set default parameters
        self.moving_left = False
        self.moving_right = False
        self.ship_speed = 0
        self.rotation_speed = 0
        self.angle = 0
        self.accelerate = False
        self.decelerate = False
        self.fire = False
        self.lives = ai_settings.ship_lives
        
        self.ship_speed_max = ai_settings.ship_speed_max
        self.ship_speed_factor = ai_settings.ship_speed_factor
        self.rotation_speed_max = ai_settings.ship_rotation_speed_max
        self.rotation_speed_factor = ai_settings.ship_rotation_speed_factor
        
        
        
        
    def update(self):
        
                #How fast ship rotates when standing still
        if not self.accelerate:
            self.rotation_speed_max_new = self.rotation_speed_max * 1.5
        else:
            self.rotation_speed_max_new = self.rotation_speed_max / 1.5
        
        #ROTATE LEFT
        if self.moving_left:
            if self.rotation_speed > -self.rotation_speed_max_new:
                self.rotation_speed -= self.rotation_speed_factor
        elif self.rotation_speed <= -self.rotation_speed_factor:
            self.rotation_speed += self.rotation_speed_factor
        
        #ROTATE RIGHT 
        if self.moving_right:
            if self.rotation_speed < self.rotation_speed_max_new:
                self.rotation_speed += self.rotation_speed_factor
        elif self.rotation_speed >= self.rotation_speed_factor:
            self.rotation_speed -= self.rotation_speed_factor
        
        #STABILIZE ROTATION
        if self.rotation_speed != 0 and (self.rotation_speed < self.rotation_speed_factor and self.rotation_speed > -self.rotation_speed_factor):
                self.rotation_speed = 0
        
        #ACCELERATE    
        if self.accelerate and self.rect.right < self.screen_rect.right and self.rect.bottom < self.screen_rect.bottom and self.rect.left > self.screen_rect.left and self.rect.top > self.screen_rect.top:
            if self.ship_speed < self.ship_speed_max:
                self.ship_speed += self.ship_speed_factor
        else:
            #set ship_speed to 0 if the numbers are too small but not 0    
            if self.ship_speed != 0 and (self.ship_speed < self.ship_speed_factor and self.ship_speed > -self.ship_speed_factor):
                self.ship_speed = 0
                
            elif self.ship_speed > 0:
                self.ship_speed -= self.ship_speed_factor
            elif self.ship_speed < 0:
                self.ship_speed += self.ship_speed_factor
            
            
        
        #Ship rotation is not faster than the ship speed, except if standing still
        if self.rotation_speed > self.ship_speed and self.ship_speed > 0:
            self.rotation_speed = self.ship_speed
        elif (self.rotation_speed * -1) > self.ship_speed and self.ship_speed > 0:
            self.rotation_speed = self.ship_speed * -1


        
        #Update direction and position of the ship
        if self.rotation_speed != 0:
            # Rotate the direction vector and then the image.
            self.direction.rotate_ip(self.rotation_speed)
            self.angle += self.rotation_speed
            self.image = pygame.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
                
        self.position += self.direction * self.ship_speed
        self.rect.center = self.position
        
        #Limit the reach of the ship
        
        if self.rect.right > self.screen_rect.right or self.rect.bottom > self.screen_rect.bottom or self.rect.left < self.screen_rect.left or self.rect.top < self.screen_rect.top:
            self.ship_speed = self.ship_speed * -1
            self.rotation_speed = 0
    
        if self.lives == 0:
            print("GAME OVER")
        
    def collision(self):
        self.ship_speed = self.ship_speed * -1
        self.rotation_speed = 0
    
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)