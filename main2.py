import pygame



pygame.init()

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
    dugtrio = pygame.transform.scale(dugtrio, (250, 250))


    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        x -= 10
    if key[pygame.K_d] == True:
        x += 10
    if key[pygame.K_w] == True:
        y -= 10
    if key[pygame.K_s] == True:
        y += 10    
    pygame.display.flip()

    pygame.display.flip()
    pygame.display.update()
pygame.quit()
