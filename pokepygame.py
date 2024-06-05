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

# main menu 
def main_menu():
    pygame.display.set_caption("Main menu")
    while True:
        Menu_Mouse_POS = pygame.mouse.get_pos()
        Menu_Text = get_font(100)
        


# makes framerate
framerate = 60
timer =  pygame.time.Clock()
animation = 0
#main character properties
mc_speed = 0.8
mc_x_position = 500 
mc_y_position = 500 

#standing still in front 
mc = pygame.image.load("sprites/mc.png")
screen.blit(mc,(mc_x_position,mc_y_position))

#moving/stand right 
mc_right = pygame.image.load("sprites/mc_right_side.png")


#moving/standing left 


#making bg image
background = pygame.image.load("sprites/background.png")
background = pygame.transform.scale(background, (1000, 1000))

# pokemon image
dugtrio = pygame.image.load("sprites/dugtrio.png")
dugtrio = pygame.transform.scale(dugtrio, (100, 100))
dugtrio_x_position = 0
dugtrio_y_position = 0

run = True
while run:
    timer.tick(framerate)
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #makes mc bigger pr smaller 
    mc_right = pygame.transform.scale(mc_right, (90,90))
    mc = pygame.transform.scale(mc, (90,90))
    # displays pokemon
    screen.blit(dugtrio,(dugtrio_x_position, dugtrio_y_position))
    #displays main character
    
    # movment 
    key = pygame.key.get_pressed() 
    if key[pygame.K_a] == True:
        mc_x_position -= 0.8
    if key[pygame.K_d] == True:
        
        mc_x_position += 0.8
        screen.blit(mc_right,(mc_x_position,mc_y_position))
        pygame.display.update
    if key[pygame.K_w] == True:
        mc_y_position -= 0.8
    if key[pygame.K_s] == True:
        mc_y_position += 0.8  
    pygame.display.flip()
    #if user moves right the sprite switches to the right side image 
    if mc_x_position != 0:
        animation += 1 


    pygame.display.flip()
    pygame.display.update()
pygame.quit()
