# gameFont = pygame.freetype.Font("Pokemon GB.ttf", 32)
import pygame
from pygame import freetype
from pygame import event 
import sys
pygame.init()
screen = pygame.display.set_mode([600,600])
white = [255, 255, 255]
red = [255, 0, 0]
black = [0,1,0]
blue = [0,0,255]

screen.fill(white)
background = white

framerate = 60  
circle_x = 300
circle_y = 300
circle_x_direction = 10
circle_y_direction = 8
player_width = 30
player_height = 50
player_x = 300
player_y = 500

player_x_directions = 0
player_y_directions = 0
player_speed = 3

font = pygame.font.Font('freesansbold.ttf', 20)
score = 0 
timer =  pygame.time.Clock()

def update_ball_posistion():
    global circle_x 
    global circle_y 
    global circle_x_direction 
    global circle_y_direction 
    global score

    if circle_x_direction > 0:
        if circle_x < 570:
            circle_x += circle_x_direction
        else: 
            circle_x_direction *= -1
            score += 1

    elif circle_x_direction < 0:
        if circle_x > 30:
            circle_x += circle_x_direction
        else: 
            circle_x_direction *= -1
            score += 1 

    if circle_y_direction > 0:
        if circle_y < 570:
            circle_y += circle_y_direction
        else: 
            circle_y_direction *= -1
            score += 1 
    elif circle_y_direction < 0:
        if circle_y > 30:
            circle_y += circle_y_direction
        else: 
            circle_y_direction *= -1
            score += 1

            
def update_player_posistion():
    global player_x 
    global player_y 
    global player_x_directions
    global player_y_directions
    if player_x_directions > 0:
        if player_x < 600 - player_width:
            player_x += player_x_directions * player_speed

    if player_x_directions < 0:
        if player_x > 0 :
            player_x += player_x_directions * player_speed

    if player_y_directions > 0:
        if player_y < 600 - player_height:
            player_y += player_y_directions * player_speed

    if player_y_directions < 0:
        if player_y > 0 :
            player_y += player_y_directions * player_speed

# # Making icon picture 
# icon = pygame.image.load("/houndour.png")
# # calling the icon
# pygame.display.set_icon(icon)

# Making the window name 
pygame.display.set_caption("My program")
pygame.display.flip()

running = True
while running:
    timer.tick(framerate)
    update_ball_posistion()
    update_player_posistion()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((background))
    pygame.draw.circle(screen, red , (circle_x,circle_y), 30 , 5)
    pygame.draw.circle(screen, black , (circle_x,circle_y), 20 )
    pygame.draw.circle(screen, white , (circle_x,circle_y), 15 )

    pygame.draw.rect(screen,blue,[player_x,player_y,player_width,player_height])
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if key[pygame.K_a] == True:
        x -= 0.8
    if key[pygame.K_d] == True:
        x += 0.8
    if key[pygame.K_w] == True:
        y -= 0.8
    if key[pygame.K_s] == True:
        y += 0.8  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_directions = 0
            if event.key == pygame.K_RIGHT:
                player_x_directions = 0
            if event.key == pygame.K_UP:
                player_y_directions = 0  
            if event.key == pygame.K_DOWN:
                player_y_directions = 0            


    
    pygame.display.update()
    display_score = font.render("score: " + str(score), True, white, black)
    screen.blit(display_score, ( 10 , 10 ))
    pygame.display.flip()

pygame.quit














def intro():
    intro =  True

    while intro:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.QUIT()
                quit()

