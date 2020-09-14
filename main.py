#Based on the penniless pilgrim riddle from Ted-Ed

import pygame
from pygame import mixer
#Initialization of pygame
pygame.init()

#Create the Screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('background.png')


#Title and Icon
pygame.display.set_caption("Tax Evador")
icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(icon)

#Temple Image
templeImg = pygame.image.load('temple_icon.png')
templeX = 736
templeY = 536

def temple(x,y):
    screen.blit(templeImg, (x,y))


#Player Image
playerImg = pygame.image.load('player_icon.png')
playerX = 16
playerY = 16
playerX_change = 0
playerY_change = 0
tax = 0
font = pygame.font.SysFont("comicsansms", 32)
playerXpast = []
playerYpast = []
#Home Screen


def player(x,y):
    screen.blit(playerImg, (x,y))

def temple(x,y):
    screen.blit(templeImg, (x,y))

#Score calculator
def tax_update(oper):
    global tax
    if oper == 'add':
        tax = tax+2
    elif oper =='sub':
        tax = tax-2
    elif oper =='mul':
        tax = tax*2
    elif oper == 'div':
        tax = tax/2
    press = 'ready'

def dont_update():
    global tax
    tax += 0

def check_past(playerx,playery, player_change_x, player_change_y):
    global playerXpast, playerYpast, playerX_change, playerY_change
    j = len(playerYpast)
    for i in range(j):
        if playerx+player_change_x == playerXpast[i]:
            if playery+player_change_y == playerYpast[i]:
                playerX_change = 0
                playerY_change = 0
                dont_update()

def path_draw(x,y):
    pygame.draw.line(screen, (0, 0, 255), (x, y), (200, 100))


# Dispplay Score
def show_score(tax_val):
    score = font.render("Score: " + str(tax_val), True, (0,255,0))
    screen.blit(score, (0,500))
#Game
over_font = pygame.font.SysFont("comicsansms", 64)
def game_over(tax_val):
    if tax_val==0:
        over_text = font.render("Congratulations!!!" , True, (0, 255, 0))
        over_text1 = font.render("You reached paying Zero tax.", True, (0, 255, 0))
        screen.blit(over_text, (265,200))
        screen.blit(over_text1, (260, 250))
    else:
        over_text1 = font.render("GAME OVER", True, (255, 0, 0))
        over_text = font.render("Try again. Tax: " + str(tax_val), True, (255, 0, 0))
        screen.blit(over_text1, (270, 200))
        screen.blit(over_text, (260, 250))

#Player Movement


running = True

while running:
    pygame.time.delay(100)
    # RGB Values
    screen.fill((1, 1, 1))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if templeY-playerY < 20 and templeX-playerX <20:
            game_over(tax)

        # If keystroke is pressed, check whether left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if playerX < 32:
                    dont_update()
                    playerX_change = 0

                elif playerX >= 32:
                    tax_update('sub')
                    playerX_change = -176
                    playerXpast.append(playerX)

            if event.key == pygame.K_RIGHT:
                if playerX >700:
                    dont_update()
                    playerX_change = 0
                elif playerX <= 700:
                    tax_update('add')
                    playerX_change = 176
                    playerXpast.append(playerX)

            if event.key == pygame.K_UP:
                if playerY < 32:
                    dont_update()
                    playerY_change = 0
                elif playerY >= 32:
                    tax_update('div')
                    playerY_change = -126
                    playerYpast.append(playerY)

            if event.key == pygame.K_DOWN:
                if playerY > 500:
                    dont_update()
                    playerY_change = 0
                elif playerY <= 500:
                    tax_update('mul')
                    playerY_change = 126
                    playerYpast.append(playerY)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                playerX_change = 0
                playerY_change = 0

            if event.key == pygame.K_RIGHT:
                playerX_change = 0
                playerY_change = 0

            if event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

            if event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

        check_past(playerX,playerY, playerX_change, playerY_change)
        playerX += playerX_change
        playerY += playerY_change

    # Checking and restricting boundary for player
    if playerX <= 0:
        playerX = 16
        playerX_change= 0
    elif playerX >= 720:
        playerX = 720
        playerX_change= 0
    if playerY <= 0:
        playerY = 16
        playerY_change = 0
    elif playerY >= 520:
        playerY = 520
        playerY_change = 0

    player(playerX, playerY)
    
    temple(templeX,templeY)
    show_score(tax)
    if playerX==720 & playerY==550:
        game_over(tax)
    pygame.display.update()
