import pygame 
from random import randint
from apple import apple
pygame.init()

screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

step = 20
x=0
y=0
dx=1
dy=0
width =380
height = 280
apple_x_dx=randint(0,19)
apple_y_dy=randint(0,14)  
scores=0
gscores=0
t=0
level =1
indicator_score=0





#map
f=open('maps/map1.txt','r')
a=f.readlines()
arr1=[] 
for i in range(15):
    for j in range(20): 
        if a[i][j]=='#':
            arr1.append((j,i))
f.close()
f=open('maps/map2.txt','r')
a=f.readlines()
arr2=[] 
for i in range(15):
    for j in range(20): 
        if a[i][j]=='#':
            arr2.append((j,i))
f.close()
f=open('maps/map3.txt','r')
a=f.readlines()
arr3=[] 
for i in range(15):
    for j in range(20): 
        if a[i][j]=='#':
            arr3.append((j,i))
f.close()




file=open('best.txt','w+')





#text
over_text=pygame.font.Font('Boldonse/Boldonse-Regular.ttf',40)
text_surface = over_text.render('Game over', False, 'White')
score_bar =pygame.font.Font('Boldonse/Boldonse-Regular.ttf',20)
level_bar =pygame.font.Font('Boldonse/Boldonse-Regular.ttf',20)




#timer
timer_event =pygame.event.custom_type()
pygame.time.set_timer(timer_event,10000)


body=[(x,y)]



run=True
over_indicator=True
while run:
    if over_indicator:
        screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        # timer
        if event.type ==timer_event:
            apple_x_dx=randint(0,19)
            apple_y_dy=randint(0,14)

    #bars
    score_bar_surface = score_bar.render(f'Score {indicator_score}', False, 'White')
    level_bar_bar_surface = level_bar.render(f'Level {level}', False, 'White')


    #moves
    if over_indicator:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and dx!=1:    
            dx=-1
            dy=0
        if keys[pygame.K_RIGHT] and dx!=-1:
            dx=1
            dy=0
        if keys[pygame.K_UP] and dy!=1:
            dx=0
            dy=-1
        if keys[pygame.K_DOWN] and dy!=-1:
            dx=0
            dy=1
        # Move head
        x += step * dx
        y += step * dy    
        if x>width:
            x=0
        if x<0:
            x=width
        if y>height:
            y=0
        if y<0:
            y=height
        


    #map 
    if gscores < 3:
        arr = arr1
        t = 1
        level = 1
    elif 3 <= gscores < 6:
        arr = arr2
        t = 2
        level = 2
    elif 6 <= gscores < 9:
        arr = arr3
        t = 4
        level = 3
    elif gscores >= 9:
        gscores = 0
        arr = arr1
        t = 1
        level = 1

    #map walls
    for i in arr:
        pygame.draw.rect(screen, 'yellow', (i[0] * 20, i[1] * 20, 20, 20))


    


    

    
    


    #meal for snake
    apple_x=apple_x_dx*20
    apple_y=apple_y_dy*20
    pygame.draw.rect(screen, 'green', (apple_x, apple_y, 20, 20))
    if apple_x==x and apple_y==y:
        apple_x_dx=randint(0,19)
        apple_y_dy=randint(0,14)
        value =randint(1,5)
        gscores+=1
        indicator_score+=value
    #checking if smth faces with walls
    for i in arr:
        if i[0]*20==apple_x and i[1]*20==apple_y:
            apple_x_dx=randint(0,19)
            apple_y_dy=randint(0,14)
        if i[0]*20==x and i[1]*20==y:
            over_indicator=False
            screen.fill('Black')
            screen.blit(text_surface,(65,100))
    
    
    #texts in screen
    screen.blit(score_bar_surface,(20,320))
    screen.blit(level_bar_bar_surface,(280,320))

    


    #rec
    if over_indicator:
        #Add new head position to the front of body
        body.insert(0, (x, y))

        #If apple was not eaten, remove the tail (to keep the length)
        if (x, y) != (apple_x, apple_y):
            body.pop()
        else:
            #Generate new apple
            apple_x_dx = randint(0, 19)
            apple_y_dy = randint(0, 14)
        pygame.draw.rect(screen, 'red', (body[0][0], body[0][1], 20, 20))  # Head
        for segment in body[1:]:
            pygame.draw.rect(screen, 'blue', (segment[0], segment[1], 20, 20))  # Tail


    

    
    
    



    #lines
    if over_indicator:
        for d1x in range(20,401,20):
            pygame.draw.line(screen,'grey',(d1x,0),(d1x,300))
        for d1y in range(20,301,20):
            pygame.draw.line(screen,'grey',(0,d1y),(400,d1y))
    


    

    pygame.display.update()
    clock.tick(5+t)
    pygame.display.flip()
file.close()
    
pygame.quit()
