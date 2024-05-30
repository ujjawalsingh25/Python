import pygame
import random
import math

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
current_time = 0
prev_time = 0

from pygame import mixer
        # Mixer -> It is a class use to handle all kind of music like repeating music, loading music.

pygame.init()   # To initialize the pygame


# Screen will created with size(800,600) -> (x,y) or (width,length) size
screen = pygame.display.set_mode((550,600))

# Background
background = pygame.image.load('bg.png')

# Background Sound
mixer.music.load('bgm.mp3')         # to load the sound
mixer.music.play(-1)                # Play music whole game period

# Display
pygame.display.set_caption("Space")       # Title of the name of the application.
icon = pygame.image.load('ufo.png')       # variable(icon) containing the icon of application.
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('jet.png')        # Get the image to set on the game screen
playerX=245                        # Set x coordinate of image or player
playerY=470                         # Set y coordinate of image or player
playerX_change = 0

# Enemy
enemyImg = []
enemyX= []                 # Set list of images
enemyY= []                 # Set random by (random int) y coordinate of enemy image
enemyX_change = []
enemyY_change = []
num_of_enemy = 5
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('emy.png'))        # Get the enemy image to set on the game screen
    enemyX.append(random.randint(15,420))                 # Set random by (random int) x coordinate of enemy image
    enemyY.append(random.randint(50,100))                 # Set random by (random int) y coordinate of enemy image
    enemyX_change.append(2.5)
    enemyY_change.append(50)

# Bullet
bulletImg = pygame.image.load('bullet.png')        # Get the enemy image to set on the game screen
bulletX = 0                # Set random by (random int) x coordinate of enemy image
bulletY = 600               # Set random by (random int) y coordinate of enemy image
bulletX_change = 0
bulletY_change = 45.2
bullet_state="ready"
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

# Score
score_value = 0
score_text = pygame.font.Font('freesansbold.ttf',32)
textX_coordinate = 20
textY_coordinate = 20

def show_score(x,y):
    score = score_text.render("Score : "+ str(score_value), True, (0,0,0))
    screen.blit(score, (x, y))

# Game Over Text
gameover_text = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    endgame = gameover_text.render(" GAME OVER ", True, (255, 0, 0))
    screen.blit(endgame,(80,200))
    show_score(180,250)


def draw_player(x,y):
    screen.blit(playerImg,(x,y))       # Draw the image in the screen and it need all the time so
                                                # kept in function and run in loop but always after screen.fill(())
                                            # otherwise it will be benith screen bg colour.

def draw_enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))         # Draw the image of enemy

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 16))

# def collision(enemyX, enemyY, bulletX, bulletY):
#     distance = math.sqrt((((enemyX - bulletX) ** 2) + ((enemyY - bulletY) ** 2)))
#     if distance < 15:           # if distance between both image pixel will be 15 then collision.
#         return True
#     else:
#         return False

def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    if distance < 27:  # Adjust this value as needed
        return True
    else:
        return False



# Loop
running = True
while running:                              # for running infinite till close the tab.

    screen.fill((0, 0, 0))  # For black screen (Always at top so that other image will draw over it
                        # otherwise all image or player of game will be benith screen background colour.
    """ Red screen --> screen.fill((255,0,0))   # (r,g,b) are the red,green,blue colours for  background since
                                                all colour are made of 'r,g,b' and range from 0 to 255 """

    screen.blit(background,(0,0))

    #  --------------------- Hand Tracking -----------------
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmarks.landmark):
                h, w, c = img.shape
                pos_x, pos_y = int(lm.x * w), int(lm.y * h)
                print(id, pos_x, pos_y)
                if id == 8:
                    cv2.circle(img, (pos_x, pos_y), 12, (0, 0, 0), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS)

    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    # Hand Tracking -------------------

    # Operate with key
    for event in pygame.event.get():        # To check in event
        if event.type == pygame.QUIT:       # OR when close button pressed to close tab
            running = False                 # To get out of while loop since tab closes

        if event.type == pygame.KEYDOWN:  # When key pressed
            # print("Key Pressed\n")
            if event.key == pygame.K_LEFT:  # If left key pressed **************
                playerX_change = -12.8
                # print("Left arrow pressed\n")
            if event.key == pygame.K_RIGHT:  # If right key pressed **************
                playerX_change = 12.8
                # print("Right arrow pressed\n")
            if event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()                             # Play bullet sound when fire
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change == 0
                # print('Key released\n')


     # Operate with hand
    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmarks.landmark):
                h, w, c = img.shape
                pos_x, pos_y = int(lm.x * w), int(lm.y * h)
                print(id, pos_x, pos_y)
                if id == 8:
                    cv2.circle(img, (pos_x, pos_y), 12, (0, 0, 0), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS)
            if pos_x in range(30,120):  # If left key pressed **************
                playerX_change = 12.5
            if pos_x in range(121,320):  # If right key pressed **************
                playerX_change = -12.5
            if pos_y in range(21, 380):
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()                             # Play bullet sound when fire
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                    if pos_y in range(21, 380):
                        playerX_change == 0

    playerX += playerX_change       # Change the coordinates on every press

    # Boundary
    if playerX <=8:              # if x decrease to last if again print at last, at very fast rate that can't visible
        playerX=8
    elif playerX >= 420:         # if x increase to last if again print at last, at very fast rate that can't visible
        playerX=420

    # Enemy Movement
    for i in range(num_of_enemy):
        # Game Over
        if enemyY[i] > 420:
            for j in range(num_of_enemy):
                enemyY[j] = 2000         # Out of screen pixel size to print out of screen or remove enemy when gameover
            game_over_text()
            break

        #  Moving
        enemyX[i] += enemyX_change[i]  # Change the coordinates on every press
        if enemyX[i] <= 15:  # if x decrease to last if again print at last, at very fast rate that can't visible
            enemyX_change[i] = 5.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 420:  # if x increase to last if again print at last, at very fast rate that can't visible
            enemyX_change[i] = -5.3
            enemyY[i] += enemyY_change[i]

        # Collision
        collided = collision(enemyX[i]+16, enemyY[i]+16, bulletX+16, bulletY+16)
        if collided:
            bullet_sound = mixer.Sound('collision.wav')
            bullet_sound.play()                             # Play explosion sound when colloid
            bulletY = 60
            bullet_state = "ready"
            score_value += 5
            print(score_value)
            enemyX[i] = random.randint(15, 420)
            enemyY[i] = random.randint(50, 100)
        draw_enemy(enemyX[i], enemyY[i], i)  # Call the function that draw the enemy over the screen


    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    draw_player(playerX, playerY)  # Call the function that draw the player over the screen
    show_score(textX_coordinate,textY_coordinate)
    pygame.display.update()  # Need to update screen every time since the display change with each action



    cv2.imshow("Image", img)
    cv2.waitKey(1)


