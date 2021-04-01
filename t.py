import math
import pygame
from pygame.math import Vector2

def newBack(x,y,speed,angle):
    new_x = x + (speed*math.cos(angle))
    new_y = y + (speed*math.sin(angle))
    return new_x, new_y
def newForward(x,y,speed,angle):
    new_x = x - (speed*math.cos(angle))
    new_y = y - (speed*math.sin(angle))
    return new_x, new_y

pygame.init()
window = pygame.display.set_mode((1000, 1000))
player = pygame.transform.smoothscale(pygame.image.load("starship.png").convert_alpha(), (32, 32))

correction_angle = 90 #lmao

run = True
player_pos  = window.get_rect().center
player_rect = player.get_rect(center = player_pos)
speed = 10
while run:
    pygame.time.delay(25) # miliseconds?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle


    keys = pygame.key.get_pressed()
    #print(player_rect)
    if keys[pygame.K_w]:
        p = newForward(player_rect.centerx,player_rect.centery,speed,math.radians(angle))
        #player_rect.centery -= speed
        player_rect.centerx = p[1]
        player_rect.centery = p[0]
    if keys[pygame.K_a]:
        player_rect.centerx -= speed
    if keys[pygame.K_s]:
        p = newBack(player_rect.centerx,player_rect.centery,speed,math.radians(angle))
        #player_rect.centery -= speed
        player_rect.centerx = p[1]
        player_rect.centery = p[0]
    if keys[pygame.K_d]:
        player_rect.centerx += speed
    #print(player_rect)
    #print("BR")

    rot_image      = pygame.transform.rotate(player, angle)
    rot_image_rect = rot_image.get_rect(center = (player_rect.centerx,player_rect.centery))

    window.fill((0, 0, 0))
    window.blit(rot_image, rot_image_rect.topleft)
    pygame.display.flip()

pygame.quit()
exit()
