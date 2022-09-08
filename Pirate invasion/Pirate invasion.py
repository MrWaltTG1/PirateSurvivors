from matplotlib.pyplot import xlim
import pygame

from Settings import Settings
from ship2 import Ship
from treasure_island import Island
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pirate invasion")
    
    #make a ship
    ship = Ship(ai_settings, screen)
    island = Island(screen, ai_settings)
    cannonballs = []
    enemies = []
    explosions = []
    ripples = []
    
    
    while True:
        clockobject = pygame.time.Clock()
        clockobject.tick(60)
        
        gf.check_events(ai_settings, screen, ship, cannonballs, enemies, explosions, ripples)
        ship.update()
        island.update()
        for x in cannonballs:
            x.update(ripples)
        for y in enemies:
            y.update()
        for z in explosions:
            z.update()
        for a in ripples:
            a.update(ripples)
        gf.collision_checks(ai_settings, screen, ship, cannonballs, enemies, island)
        gf.update_cannonballs(enemies, cannonballs, screen, explosions, ai_settings)
        gf.update_screen(ai_settings, screen, ship, cannonballs, enemies, explosions, ripples, island)



run_game()