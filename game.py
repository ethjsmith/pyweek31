import pygame
class Ball(pygame.sprite.Sprite):

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
pygame.init()

screen = pygame.display.set_mode([500,500])

running = True
ball = Ball()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    ball.update()
    #pygame.draw.circle(screen,(0,255,255),(250,250),75)
    pygame.display.flip()
pygame.quit()


# class bandit(Sprite):
#     def __init__ (self,screen,img_filename,init_position,init_direction,speed):
