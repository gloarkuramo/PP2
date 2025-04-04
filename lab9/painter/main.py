import pygame 

pygame.init()
screen=pygame.display.set_mode((600,600))
x,y=0,0
positions=[]
positions_erase=[]
positions_rec=[]
positions_cir=[]
positions_right_triangle=[]
positions_equivalence_triangle=[]
positions_rhoumbus=[]

colors=['blue','red','green']
index_color=0

run=True
draw=False
erase=False
rec=False
cir=False
right_triangle=False
equivalence_triangle=False

det_draw='draw'

# 



while run:
    screen.fill((0,0,0))
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run=False
            if event.key==pygame.K_d:
                det_draw='draw'
            if event.key ==pygame.K_e and keys[pygame.K_LSHIFT]:
                det_draw='erase'
            if event.key ==pygame.K_o and keys[pygame.K_LSHIFT]:
                det_draw='rectengular'
            if event.key ==pygame.K_t and keys[pygame.K_r]:
                det_draw='right_triangle'
            if event.key ==pygame.K_t and keys[pygame.K_e]:
                det_draw='equivalence_triangle'
            if event.key==pygame.K_c and keys[pygame.K_LSHIFT]:
                det_draw='circle'
            if event.key==pygame.K_r:
                det_draw='rhoumbus'
            if event.key==pygame.K_b:
                index_color=0
            
            if event.key==pygame.K_g:
                index_color=2
        
        #det a mouse position
        if event.type ==pygame.MOUSEMOTION:
            x,y=pygame.mouse.get_pos()
        if event.type ==pygame.MOUSEBUTTONDOWN:
            draw=True
            #drawing triangle 
            if det_draw=='right_triangle':
                draw=False
                positions_right_triangle.append((x,y))
            if det_draw=='equivalence_triangle':
                draw=False
                positions_equivalence_triangle.append((x,y))
            if det_draw=='rhoumbus':
                draw=False
                positions_rhoumbus.append((x,y))
        


        if event.type ==pygame.MOUSEBUTTONUP:
            draw=False


       

    
        
    
    #adding positions to arrays 
    if draw:
        if det_draw=='erase':
            positions_erase.append((x,y))
        elif det_draw=='rectengular':
            positions_rec.append((x,y,50,50))
        elif det_draw=='circle':
            positions_cir.append((x,y))
        elif det_draw=='draw':
            positions.append((x,y))

    
    #others 
    for i in positions_rec:
        pygame.draw.rect(screen,colors[index_color],i,3)

    for i in positions_cir:
        pygame.draw.circle(screen,colors[index_color],i,20,3)

    for i in positions:
        pygame.draw.circle(screen,colors[index_color],i,20)

    


   #drawing right triangle
    for i in positions_right_triangle:
        pygame.draw.polygon(screen, colors[index_color], [
            (i[0], i[1]),             
            (i[0] + 100, i[1]),       
            (i[0], i[1] + 100)        
        ], 3)


    #drawing equinvalence triangle
    for i in positions_equivalence_triangle:
        pygame.draw.polygon(screen,colors[index_color],[
            (i[0],i[1]),
            (i[0]-50,i[1]+100),
            (i[0]+50,i[1]+100)
        ],3)
    

    #drawing rhoumbus
    for i in positions_rhoumbus:
        pygame.draw.polygon(screen,colors[index_color],[
            (i[0],i[1]+25),
            (i[0]+50,i[1]),
            (i[0],i[1]-25),
            (i[0]-50,i[1])
        ],3)
    

    #eraser
    for i in positions_erase:
        pygame.draw.circle(screen,'black',i,20)

        



    pygame.display.flip()
    pygame.display.update()


pygame.quit()

