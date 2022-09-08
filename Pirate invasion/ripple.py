import pygame

class Ripple():

    def __init__(self, ai_settings, screen, pos=(0,0)):
        self.screen = screen
        self.image = pygame.image.load("Pirate invasion/images/ripple1.bmp")
        self.original_image = self.image
        self.position = pos
        
        self.time_max = ai_settings.ripple_timer * 1000
        self.starttime = pygame.time.get_ticks()
        self.endtime = self.starttime + self.time_max
        self.percentage = (self.time_max / ai_settings.ripple_percent) / 100
        self.new_percentage = self.percentage
        self.reverse_percentage = (100 - self.new_percentage) / 100
        
        self.imagex = 500 * self.reverse_percentage
        self.image = pygame.transform.scale(self.image, (self.imagex,self.imagex))
        
    def update(self, list):
        self.current_time = pygame.time.get_ticks()
        self.time_left =  self.endtime - self.current_time
        
        if self.time_left <= 0:
            list.remove(self)
            
        
        
        if self.time_left <= (self.time_max - self.new_percentage):
            self.new_percentage += self.percentage
            self.reverse_percentage = (100 - self.new_percentage) / 100
            if self.imagex >= 0: self.imagex = 70 * self.reverse_percentage
            self.image = pygame.transform.scale(self.original_image, (self.imagex,self.imagex))
        self.rect = self.image.get_rect(center=self.position)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)