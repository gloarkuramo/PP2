import pygame
def apple(dx,dy,x,y,apple_x_dx,apple_y_dy):
    apple_x=apple_x_dx*20
    apple_y=apple_y_dy*20
    pygame.draw.rect(screen, 'green', (apple_x, apple_y, 20, 20))
    if apple_x==x and apple_y==y:
        apple_x_dx=randint(0,19)
        apple_y_dy=randint(0,14)
        scores+=1
        gscores+=1
    #checking if smth faces with walls
    for i in arr:
        if i[0]*20==apple_x and i[1]*20==apple_y:
            apple_x_dx=randint(0,19)
            apple_y_dy=randint(0,14)
        if i[0]*20==x and i[1]*20==y:
            over_indicator=False
            screen.fill('Black')
            screen.blit(text_surface,(65,100))