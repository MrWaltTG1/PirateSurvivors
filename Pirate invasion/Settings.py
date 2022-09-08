from random import randint
import pygame


class Settings():
    """A class the store all settings"""
    
    def __init__(self):
        """initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = pygame.image.load("Pirate invasion/images/Ocean.bmp")
        self.bg = pygame.transform.scale(self.bg, (1200, 800))
        self.rect = self.bg.get_rect()
        
        #Ship settings
        self.ship_image = pygame.image.load("Pirate invasion/images/pirateship.bmp")
        self.ship_image = pygame.transform.scale(self.ship_image, (80, 40))
        #Ship speeds
        self.ship_speed_factor = 0.3
        self.ship_speed_max = 5
        self.ship_rotation_speed_factor = 0.3
        self.ship_rotation_speed_max = 5
        #Ship position
        self.ship_pos = (750,400)
        
        self.ship_lives = 3
        
        
        #Enemy ship settings
        self.enemy_image = pygame.image.load("Pirate invasion/images/enemy.bmp")
        self.enemy_image = pygame.transform.scale(self.enemy_image, (70, 120))
        #Speed
        self.enemy_ship_speed = 1
        
        
        
        #Cannonball settings
        self.cannonball_speed_factor = 3
        self.cannonball = pygame.image.load("Pirate invasion/images/cannonball.bmp")
        self.cannonball = pygame.transform.scale(self.cannonball, (10, 10))
        self.cannonball_width = self.cannonball.get_width()
        self.cannonball_height = self.cannonball.get_height()
        self.cannonball_timer = 1.5 #time in seconds
        
        #Explosion Settings
        self.explosion_timer = 2 #in seconds
        self.explosion_image = pygame.image.load("Pirate invasion/images/explosion.bmp")
        self.explosion_image = pygame.transform.scale(self.explosion_image, (80, 80))
        
        #Ripple Settings
        self.ripple_timer = 2 #in seconds
        self.ripple_percent = 20 #5%
        
        #Island Settings
        self.island_image = pygame.image.load("Pirate invasion/images/treasure_island.bmp")
        self.island_rect = self.island_image.get_rect()
        self.island_lives = 5