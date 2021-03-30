import pygame

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites  = []
        self.sprites.append(pygame.image.load('ship1.png'))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()

class Ship(pygame.Sprite):
    def __init__(self,screen,img_filename,init_position,init_direction,speed):



pygame.init()

window = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("the game")

# this should be an object LOL
x = 50
y = 50
width =40
height = 60
vel =5
moving_sprites = pygame.sprite.Group()
me = PlayerShip(x,y)
moving_sprites.add(me)

# Good http://programarcadegames.com/index.php?chapter=introduction_to_sprites



# main loop :)
running = True
while running:
    pygame.time.delay(25) # caps fps so the game doesn't run too fast 100 MS, (maybe too slow ? )
    # check for events, so anything the user does...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyholding controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        me.rect.y -= 5
    if keys[pygame.K_a]:
        pygame.transform.rotate(me.image,15)
        window.blit(me.image,(me.rect.x,me.rect.y))
        #me.rect.x -= 5
    if keys[pygame.K_s]:
        me.rect.y += 5
    if keys[pygame.K_d]:
        me.rect.x += 5
    window.fill((0,0,0))
    moving_sprites.draw(window)
    moving_sprites.update(0.25)
    pygame.display.flip()
    #pygame.draw.rect(window,(255,0,0), (x,y,width,height))
    pygame.display.update() # this should always happen at the end of every game loop probably ?



pygame.quit() # ends the game lol
