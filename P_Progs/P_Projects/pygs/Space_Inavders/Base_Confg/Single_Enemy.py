import pygame
from pygame import mixer
import random
import math

#Initialise pygame
pygame.init()

#Window
screen = pygame.display.set_mode((814,604))    #Need to pass a tuple conveying the width and height of the screendow

#Background
background = pygame.image.load('b.png')

#Title
pygame.display.set_caption("Space Invaders")

#Icon 
#Can use flaticon.com for the image
#Select png and 32 pixel size(imgs can be resized using pygame)

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("spaceship.png")  #Specify the img
playerX = 350   #Provide the X and Y coords of the img
playerY = 480
#playerX_change = 0 

#Enemy
enemyImg = pygame.image.load("alien.png")  #Specify the enemy img
enemyX = random.randint(0,750)   #Provides randomised value of X and Y coords of enemy
enemyY = random.randint(50,150)
enemyX_change = 0.1
enemyY_change = 20

#Bullet

#Ready = bullet not visible
#Fire = bullet visible(moving)
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480 
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

#Score
score_value = 0  

#Font is defined
font = pygame.font.Font('freesansbold.ttf', 32)     #Free font present in pygame, size

#It's coords to be displayed are given
textX = 10
textY = 10

def show_score(x,y):

    #Rendering the font                 #("text", T/F for display, font colour(R,G,B))
    score = font.render("Score: " + str(score_value), True, (255,255,255))
                        
    #Displaying score on screen
    screen.blit(score ,(x,y))

#Game over font defined
over_font =  pygame.font.Font('freesansbold.ttf', 64)

#Game over text
def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255,255,255))            
    screen.blit(over_text,(200,250))


def player():

    #blit method is used to print the img on the screen at the passed coords
    screen.blit(playerImg,(playerX,playerY))


def enemy():

    #blit method is used to print the img on the screen at the passed coords
    screen.blit(enemyImg,(enemyX,enemyY))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2) + math.pow(enemyY - bulletY,2))

    if distance < 27:
        return True

    else:
        return False

run = True

#Game loop
while run:

    #Changes the background colour by giving RGB vals
    screen.fill((0,0,0)) 

    #Backgroud image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:   #Checks for QUIT event
            run = False

        #Check for keystroke then if it's left or right

        if event.type == pygame.KEYDOWN:    #Detects keystrokes
            
            '''if event.type == pygame.K_SPACE:     #Does not detect SPACEBAR when it is pressed
                print("Success!")
                fire_bullet(playerX,bulletY)'''

            if event.key == pygame.K_LEFT:
                
                if playerX > 0:     #Detects if the left arrow key was pressed
                    playerX_change = -50
                    playerX += playerX_change

                else:
                    playerX_change = 0
                    playerX = 0 

            if event.key == pygame.K_RIGHT:
                
                if playerX < 750:     #Detects if the left arrow key was pressed
                    playerX_change = 50
                    playerX += playerX_change

                else:
                    playerX_change = 0
                    playerX = 750

        #Detects keystroke releases
        if event.type == pygame.KEYUP:      #Detects SPACEBAR when released     
            
            if event.key == pygame.K_SPACE:
                
                if bullet_state == "ready":

                    #Adding bullet sound
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()

                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

    
    enemyX += enemyX_change


    if enemyX <= 0:
        enemyX_change = 0.1
        enemyX += enemyX_change

        if enemyY < 480:
            enemyY += enemyY_change

    if enemyX >= 750:
        enemyX_change = -0.1
        enemyX += enemyX_change

        if enemyY < 480:
            enemyY += enemyY_change

    #Check for game over
    if enemyY > 440:
        enemyY = 2000
        game_over_text()

    #Bullet Movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    #Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)

    if collision:

        #Adding bullet sound
        explosion_sound = mixer.Sound('explosion.wav')
        explosion_sound.play()

        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        #print(score_value)
        enemyX = random.randint(0,750)   #Spawns enemy at new location
        enemyY = random.randint(50,150)
     

        
    player()    #Should come after screen.fill otherwise it will not be visible
    show_score(textX, textY)
    enemy()
    pygame.display.update() #Required to reflect any changes made on the screen

pygame.quit()