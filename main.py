import pygame



pygame.init()


#Screen witdh and screen height
screen_width = 1000
screen_height = 1000
#This is used to display the screen
screen = pygame.display.set_mode((screen_height, screen_width))
#adding image/customizing image


# the player that moves
player = pygame.Rect((300, 250, 50, 50))


#The game loop[]
run = True
while run: 
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)   
    
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

    pygame.display.update()
pygame.quit()


# dugtrio_top = screen.get_height() - dugtrio.get_height()
# dugtrio_left = screen.get_width()/2 - dugtrio.get_width()/2

