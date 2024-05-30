import pygame
from pygame import mixer


pygame.init()
mixer.init()
#loadingthe music 

#Screen witdh and screen height
screen_width = 1000
screen_height = 1000
#This is used to display the screen
screen = pygame.display.set_mode((screen_height, screen_width))



#making bg image
background = pygame.image.load("./background.png")
background = pygame.transform.scale(background, (1000, 1000))

# pokemon image
dugtrio = pygame.image.load("./dugtrio.png")
mc = pygame.image.load("./mc.png")
x = 0
y = 0

run = True
while run:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # displays pokemon
    screen.blit(dugtrio,(x,y))
    dugtrio = pygame.transform.scale(dugtrio, (100, 100))
    #displays main character


    screen.blit(mc,(x,y))
    mc = pygame.transform.scale(mc, (90,90))
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        x -= 0.8
    if key[pygame.K_d] == True:
        x += 0.8
    if key[pygame.K_w] == True:
        y -= 0.8
    if key[pygame.K_s] == True:
        y += 0.8  
    pygame.display.flip()

    pygame.display.flip()
    pygame.display.update()
pygame.quit()
