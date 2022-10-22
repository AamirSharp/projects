from ast import While
from glob import glob
import pygame, sys
import random
import math


pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Due Date")


icon = pygame.image.load("Desktop/DesignSummative/iconduedate.png")
pygame.display.set_icon(icon)

endscreen = pygame.image.load("Desktop/DesignSummative/end.jpg")
background = pygame.image.load("Desktop/DesignSummative/background.jpg")
homepage = pygame.image.load("Desktop/DesignSummative/homepage.png")
portalimg = pygame.image.load("Desktop/DesignSummative/portal.png")

portX = random.randint(30, 960)
portY = random.randint(30,760)


playerimg = pygame.image.load("Desktop/DesignSummative/Astro.png")
playerX = 250
playerY = 100
playerXchange = 0
playerYchange = 0

speed = 1.5

assignmentimg = pygame.image.load("Desktop/DesignSummative/assignment.png")
moves = 0
score = 0
duedate = random.randint(3,9)
duedate = duedate - moves
randogenoX = random.randint(50,950)
randogenoY = random.randint(50,750)
preblit = False


def assignment(x,y):
    screen.blit(assignmentimg, (x, y))

def player(x, y):
    screen.blit(playerimg, (x, y))

def portal(x, y):
    global preblit
    screen.blit(portalimg, (x, y))
    preblit = True

     
myFont = pygame.font.Font("freesansbold.ttf", 32)
#textX = 10
textY = 10
textdueX = 400
scoreX = 430
scoreY = 55

portalcollide = False
collide = False
        
def showduedate(x,y):
    duedatevalue = myFont.render("Due Date: " + str(duedate-moves), True,(255,255,255))                   #Shows when the duedate is
    screen.blit(duedatevalue, (x, y))
def showscore(x,y):
    global score
    submitedtext = myFont.render("Score: " + str(score), True,(255,255,255))                        #Prints the score
    screen.blit(submitedtext, (x, y))
        
def get_font(size):
    return pygame.font.Font("freesansbold.ttf", size)
def isCollision(playerX,playerY,randogenoX,randogenoY):
    global collide
    distance = math.sqrt(math.pow(playerX - randogenoX, 2) + math.pow(playerY - randogenoY, 2))     # Checks for collsion with assignment
    if distance < 87:
        collide = True
    elif distance < -86:    
        collide = True
        #return True
    else:
        return False
    
def submmision(playerX, playerY, portX, portY):                                         # Checks for collision with portal
    global portalcollide
    distance = math.sqrt(math.pow(playerX - portX, 2) + math.pow(playerY - portY, 2))    
    if distance < 87:
        if preblit == True:
            portalcollide = True
    elif distance < -86:    
        if preblit == True:
            portalcollide = True
        #return True
    else:
        return False
def play():
    global playerY
    global playerX
    global playerXchange
    global playerYchange
    global speed
    global portalcollide
    global moves
    global mainmenu
    global score
    
    mainmenu = False
    running = True
    while running:
        screen.fill((0,0,225))
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerXchange = -3.5
                if event.key == pygame.K_RIGHT:
                    playerXchange = 3.5
                if event.key == pygame.K_UP:
                    playerYchange = -5
                if event.key == pygame.K_DOWN:
                    playerYchange = 3.5    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    moves += 1
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    moves += 1
        playerX += playerXchange
        playerY += playerYchange
        playerY += speed
        
        if collide == True:             #Checks for collisioin with Assignment
            portal(portX, portY)    
        
        if portalcollide == True:        #Checks for collision with Portal
            portalcollide = False
            score += 1
            score = (score -score)+ 1
            showscore(scoreX,scoreY)
            
                        
        if moves > duedate:             #Checks if  duedate is passed or not
            gameover()
            
            
        if playerX <= -50:              #Boundaries for the map
            playerX = -50
        elif playerX >= 920:
            playerX = 920
        if playerY <= -20:
            playerY = -20
        elif playerY >= 700:
            playerY = 700
        
        
        submmision(playerX, playerY, portX, portY)
        #showmoves(textX,textY)
        showduedate(textdueX,textY)                                     #Calling all the functions
        isCollision(playerX,playerY,randogenoX,randogenoY)
        assignment(randogenoX, randogenoY)
        player(playerX,playerY)
        showscore(scoreX, scoreY)

        #shoot(playerX)
        pygame.display.update()

def main_menu():
    global running
    mainmenu = True
    running = False
    while mainmenu:
        screen.blit(homepage,(-450,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainmenu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    play()
                    mainmenu = False
        pygame.display.update()

def gameover():
    global runnings
    endsc = True
    running = False
    while endsc:
        screen.blit(endscreen,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endsc = False
                quit()
        pygame.display.update()
        
main_menu()


