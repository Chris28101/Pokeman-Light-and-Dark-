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




run = True
while run:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    pygame.display.update()
pygame.quit()
