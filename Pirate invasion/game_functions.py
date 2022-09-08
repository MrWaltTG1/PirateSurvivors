import datetime
import random
import pygame
import sys
from cannonball import Cannonball
from explosion import Explosion
from enemy import Enemy
from ripple import Ripple
from pygame.math import Vector2

def check_keydown_events(event, ai_settings, screen, ship, cannonballs):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        #turn the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        #accelerate the ship
        ship.accelerate = True
    elif event.key == pygame.K_LEFT:
        #turn the ship left
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        pass
    
    #Shoot a cannonball
    if event.key == pygame.K_SPACE:
        new_bullet = Cannonball(ai_settings, screen, ship)
        cannonballs.append(new_bullet)
        
def check_keyup_events(event, ai_settings, screen, ship, cannonballs):
    """Respond to keyreleases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.accelerate = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def random_events(ai_settings, screen, ship, cannonballs, enemies, ripples):
        """Creates events randomly"""
        rng = random.randint(0, 100)
        if rng == 1:
            new_enemy = Enemy(ai_settings, screen, ship, cannonballs)
            enemies.append(new_enemy)
    
def check_events(ai_settings, screen, ship, cannonballs, enemies, explosions, ripples):
    #watch for keyboard and mouse events
    for event in pygame.event.get():
        #If event is quit then quit
        if event.type == pygame.QUIT:
            sys.exit
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, cannonballs)
                
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings, screen, ship, cannonballs)
        #TIMER 1 FOR EXPLOSIONS
        elif event.type == pygame.USEREVENT + 1:
            for e in explosions:
                e.timer(explosions)

    
    random_events(ai_settings, screen, ship, cannonballs, enemies, ripples)
    

def update_screen(ai_settings, screen, ship, cannonballs, enemies, explosions, ripples, island):
    #redraw the screen during each pass of the loop
    screen.blit(ai_settings.bg, ai_settings.rect)    
    ship.blitme()
    island.blitme()
    for cannonball in cannonballs:
        cannonball.blitme()
    for enemy in enemies:
        enemy.blitme()
    for boom in explosions:
        boom.blitme()
    for rip in ripples:
        rip.blitme()
    
    #Make the most recently drawn screen visible
    pygame.display.flip()
    
def update_cannonballs(enemies, cannonballs, screen, explosions, ai_settings):

    #print(cannonballs, enemies)
    #Check for collisions with enemy ships
    
    for x in enemies:
        rectx = x.rect
        for y in cannonballs:
            recty = y.rect
            collision = pygame.Rect.collidepoint(rectx, recty)
            
            
            if collision:
                enemies.remove(x)
                cannonballs.remove(y)
                new_explosion = Explosion(screen, rectx, ai_settings)
                explosions.append(new_explosion)
                print("BOOOOOOOOOM")
                
    #DESTROY WHEN OUT OF BOUNDS
    limit = 80    
    for x in enemies:
        if x.position[0] < 0 - limit or x.position[0] > 1200 + limit or x.position[1] < 0 - limit or x.position[1] > 800 + limit:
            enemies.remove(x)
    
    for y in cannonballs:
        if y.position[0] < 0 or y.position[0] > 1200 or y.position[1] < 0 or y.position[1] > 800:
            cannonballs.remove(y)
            
    #Start the cannonball timer
    for e in cannonballs:
        e.timer(cannonballs)
        
def ripple_event(screen, ai_settings, position, ripples):
    new_ripple = Ripple(ai_settings, screen, position)
    ripples.append(new_ripple)
    
    
def collision_checks(ai_settings, screen, ship, cannonballs, enemies, island):
    player_rect = ship.rect
    island_rect = island.rect
    for a in enemies:
        enemy_rect = a.rect.center
        a_collision = pygame.Rect.collidepoint(player_rect, enemy_rect)
        
        if a_collision:
            ship.lives -= 1
            ship.collision()
    
    crash_collision = pygame.Rect.collidepoint(island_rect, player_rect.center)
    if crash_collision:
        ship.collision()
        print("CRAAASH")