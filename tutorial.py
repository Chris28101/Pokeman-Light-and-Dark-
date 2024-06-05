import pygame
from pygame import freetype
import sys
pygame.init()
screen = pygame.display.set_mode([600,600])
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]

blue = [0,0,255]

screen.fill(white)
background = white

framerate = 60  
circle_x = 300
circle_y = 300
circle_x_direction = 10
circle_y_direction = 5
player_width = 30
player_height = 50
player_x = 300
player_y = 500

player_x_directions = 0
player_y_directions = 0
player_speed = 3

font = pygame.font.Font('freesansbold.ttf', 20)
game_over_font = pygame.font.Font('freesansbold.ttf', 60)
score = 0
timer =  pygame.time.Clock()

def check_collision(playerx, playery, ballx, bally):
    if abs(playerx - ballx) < 44 and abs(playery - bally) < 54:
        global player_x_directions 
        global player_y_directions
        global circle_x_direction
        global circle_y_direction
        player_x_directions = 0
        player_y_directions = 0 
        circle_x_direction = 0
        circle_y_direction = 0
        game_over()

def game_over():
    display_game_over = display_score = game_over_font.render("Game Over!!" , True, blue, black)
    screen.blit(display_score, ( 100 , 300 )) 
def intro():
    intro =  True

    while intro:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.QUIT()
                quit()

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

    screen.fill(background)
    ball = pygame.draw.circle(screen, red , (circle_x,circle_y), 30 , 5)
    player = pygame.draw.rect(screen, blue, [player_x, player_y, player_width, player_height])
    check_collision(player.centerx, player.centery, ball.centerx, ball.centery,)

    pygame.draw.circle(screen, black , (circle_x,circle_y), 20 )
    pygame.draw.circle(screen, white , (circle_x,circle_y), 15 )


    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player_x -= player_speed
    if key[pygame.K_d]:
        player_x += player_speed
    if key[pygame.K_w]:
        player_y -= player_speed
    if key[pygame.K_s]:
        player_y += player_speed

    # Ensure player doesn't go out of bounds
    if player_x < 0:
        player_x = 0
    if player_x > 600 - player_width:
        player_x = 600 - player_width
    if player_y < 0:
        player_y = 0
    if player_y > 600 - player_height:
        player_y = 600 - player_height
   
    pygame.display.flip()

    pygame.display.update()
    display_score = font.render("score: " + str(score), True, white, black)
    screen.blit(display_score, ( 10 , 10 ))
    pygame.display.flip()

pygame.quit()

w