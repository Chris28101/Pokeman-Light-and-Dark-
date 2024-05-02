import pygame



pygame.init()

# class dugtrio:

#Screen witdh and screen height
screen_width = 1000
screen_height = 1000
#This is used to display the screen
screen = pygame.display.set_mode((screen_height, screen_width))

#making bg image
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1000, 1000))
#adding image/customizing image
dugtrio = pygame.image.load("dugtrio.png")
dugtrio = pygame.transform.scale(dugtrio, (200, 200))

x = 250
y = 100

# # def trio(x,y):
# #     global dugtrio
# dugtrio = pygame.Surface([32,32])


# the player that moves
player = pygame.Rect((300, 250, 50, 50))


#The game loop[]
run = True
while run:

    screen.blit(background, (x,y))

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)   
    screen.fill((0,0,0))
    screen.blit(dugtrio, (x,y))

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_UP] == True:
        player.move_ip(0, -1) 
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, 1)       
    pygame.display.flip()
    

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    pygame.display.update()
pygame.quit()




