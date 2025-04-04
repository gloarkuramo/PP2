import pygame
from random import randint



pygame.init()
screen = pygame.display.set_mode((600,600))
FPS=pygame.time.Clock()




#images
raod=pygame.image.load('images/road.jpg')






width =600
height =600
x=0
step=6
speed=5
score=0

y=0
rand_e=randint(0,19)
#texts in screen 
score_bar =pygame.font.Font(('Boldonse/Boldonse-Regular.ttf'),20)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load('images/car.png')
        self.rect =self.image.get_rect()
        self.rect.center =(width//2,500)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-speed, 0)
        if self.rect.right < width:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(speed, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load('images/enemy.jpg')
        self.rect =self.image.get_rect()
        self.center =(randint(35,width-35),0)
    def update(self):
        self.rect.move_ip(0,step)
        if self.rect.top > 600:
            self.rect.top =0
            self.rect.center=(randint(35,width-35),0)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load('images/coins.jpeg')
        self.rect =self.image.get_rect()
        self.rect.center =(randint(40,width-40),0)
    def update(self):
        self.rect.move_ip(0,step)
        if self.rect.top >600:
            self.rect.top =0
            self.rect.center =(randint(40,width-40),0)
        
    
P1=Player()
E1=Enemy()
C1=Coins()

#CReating sprites
enemies =pygame.sprite.Group()
enemies.add(E1)

coins =pygame.sprite.Group()
coins.add(C1)

all_sprites =pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)



#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)



t=0
run=True
while run:
    screen.blit(raod,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run=False
    if score>30+t:
        step+=0.5
        speed+=0.5
        t+=30
            

    #score bars
    score_bar_surface =score_bar.render(f'Score {score}',False,'White')
    screen.blit(score_bar_surface,(0,0))

    
    #Moves and Re-draws
    all_sprites.update()
    all_sprites.draw(screen)


    

    

    #detect if coll occurs 
    if pygame.sprite.spritecollideany(P1,enemies):
        screen.fill('Red')
        pygame.display.update()
        for i in all_sprites:
            i.kill()
            run=False
    if pygame.sprite.spritecollideany(P1,coins):
        value=randint(1,5)
        score+=value
        for i in coins:
            i.rect.top=0
            i.rect.center =(randint(40,width-40),0)
            




    pygame.display.update()
    FPS.tick(60)

print(score)


pygame.quit()