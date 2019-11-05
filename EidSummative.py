# Name: Moustafa Eid
# Date: May 8 2017
# Class: ICS3U1-03
# Description: Summative - E-Hoops

# Importing all necessary sources
import pygame
import random
import math

# Initiating pygame and Creating screen
pygame.init()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)

# Define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
GREY = (142,143,147)
BROWN = (170,83,1)
ORANGE = (244,139,42)

# Declaring variables for running pygame program
running = True  # Variable that makes program run
myClock = pygame.time.Clock()   # Program that creats fps

# Number Variables
vi = 100 # Velocity variable
y = 385 # object y position
x = 90 # 0bject x position
xaim = 100 # aiming x position
yaim = 400 # aiming y position
menurun = 0 # variable to run menu
clickx = 0 # variable that stores x clicked
clicky = 0 # variable that stores y clicked
clickhistory = 0 # Variable that stores history of clicks
score = 0 # variable that stores score
speed = 1 # variable that stores speed
mousehistory = 0 # Variable that stores mouse history
menuopt = 0 # Variable that store menu option
ymove = 400 # variable that stores box y coordinate
speedy = 1 # variable that stores box y speed
colour = 0 # Variable that changes colour
gamemap = 0 # Variable that stores map
gamemode = 0 # Variable that stores mode
clickchange = 0 # Variable that stores changing mouseclicks
lives = 11 # Variable for amount of lives available
timer = 0 # Variable for timer
playstart = 0 # Variable for starting to play
count = 3000 # Variable that counts

# List Variables
scorehistory = [] # List that stores highscore for mode 1
scorehistory2 = [] # List that stores highscore for mode 2
objectx = [400] # List that stores ball x movement
objecty = [100] # List that stores ball y movement

# Random Variables
xmove = random.randint(120,700) # variable that starts forklift at random point
randomobject = random.randint(1,2) # Variable that gets random object to throw
r = random.randint(0,255) # Variable that stores a random red colour
g = random.randint(0,255) # Variable that stores a random green colour
b = random.randint(0,255) # Variable that stores a random blue colour

# Boolean Variables
change = False # boolean that stores change in clicks
mode1 = False # boolean that stores if mode 1 is true
mode2 = False # boolean that stores if mode 2 is true
lose = False # boolean that stores if you lose a life
repeat = False # boolean that stores repeated values
playgame = False # boolean that stores playing the gamemode
collide3 = False # boolean that stores collision3
time = False # boolean that stores if time ended or not
dead = False # variable for life losss
run = True # boolean to run gamemodes
click = True # boolean that checks for clicks
moveright = True # Boolean to move forklift and box right
moveleft = False # Boolean to move forklift and box left
moveup = False # Boolean to move forklift and box up
movedown = False # Boolean to move forklift and box down
objectclick = True # boolean for checking if mouse button 1 is clicked when throwing
collision1 = False # Boolean for side collision
collision2 = False # Boolean for getting a goal
collision3 = False # Boolean for bottom collision
goal = False # boolean for goals
end = False # boolean that lets you restart aiming
noclick = False # boolean that sees if mb is not clicked
escape = False # Boolean that escapes game when esc is pressed
scorey = False # Boolean that changes score to y
ballmove = False # boolean that moves ball


# All images that are used, loaded
mobilePic = pygame.image.load("14.png")
mobilePic = pygame.transform.scale(mobilePic, (20,30))
monitorPic = pygame.image.load("monitor.png")
monitorPic = pygame.transform.scale(monitorPic, (40,40))
background1menuPic = pygame.image.load("background.png")
background1menuPic = pygame.image.load("background.png")
background1menuPic = pygame.transform.scale(background1menuPic, (180,80))
background2menuPic = pygame.image.load("background2.jpg")
background2menuPic = pygame.transform.scale(background2menuPic, (180,80))
background3menuPic = pygame.image.load("background3.jpg")
background3menuPic = pygame.transform.scale(background3menuPic, (180,80))
background1Pic = pygame.image.load("background.png")
background1Pic = pygame.transform.scale(background1Pic, (800,600))
background2Pic = pygame.image.load("background2.jpg")
background2Pic = pygame.transform.scale(background2Pic, (800,600))
background3Pic = pygame.image.load("background3.jpg")
background3Pic = pygame.transform.scale(background3Pic, (800,600))
menuPic = pygame.image.load("menuscreen.jpg")
menuPic = pygame.transform.scale(menuPic, (800,600))
controlsPic = pygame.image.load("controls.png")
controlsPic = pygame.transform.scale(controlsPic, (800,600))

# Loading fonts that are used
fontback = pygame.font.SysFont("Times New Roman",50)
fontmode = pygame.font.SysFont("Times New Roman",35)
fontmenu = pygame.font.SysFont("French Script MT Regular",60)
fonttitle = pygame.font.SysFont("Stencil",80)

# Creates a rectangle for the indicator box
title = pygame.Rect(250,30,87,37)
indicator = pygame.Rect(360,150,87,37)
indicator2 = pygame.Rect (290, 300, 245, 37)
indicator3 = pygame.Rect (360, 450, 87, 37)
back = pygame.Rect(600,20,100,100)
mapchangeright = pygame.Rect(520,125,30,50)
mapchangeleft = pygame.Rect(250,125,30,50)
modechangeright = pygame.Rect(520,425,30,50)
modechangeleft = pygame.Rect(250,425,30,50)
play = pygame.Rect(710,550,62,40)
loserect = pygame.Rect(0,550,800,600)

# Loding music and sounds
menuSound = pygame.mixer.Sound("menumusic.wav")
mode1Sound = pygame.mixer.Sound("mode1.wav")
mode2Sound = pygame.mixer.Sound("mode2.wav")


# Opening High score for gamemode 1 text file and saving it to list
# Reading from a file
ScoreFile = open("score.txt", "r")
while True:
    text = ScoreFile.readline()
    if text == "":
        break
    scorehistory.append(int(text))
ScoreFile.close()

# Opening High score for gamemode 2 text file and saving it to list
# Reading from a file
ScoreFile2 = open("score2.txt", "r")
while True:
    text = ScoreFile2.readline()
    if text == "":
        break
    scorehistory2.append(int(text))
ScoreFile2.close()


# Function that gets mouse coordiantes and clicks
def getmouse ():
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()[0]
    return (mx, my, mb)

# Function that Draws box and moves it
def boxmove ():
    global moveright,moveleft,xmove,speed,ymove,speedy,moveup,movedown,rotate,boxrect,collisionrect
    if moveright == True: # if box is moving right
        xmove += speed # add speed
        if moveup == True: # if box is moving up  
            ymove -= speedy # Subtract yspeed
            if ymove <= 240: # if it reaches boundary change positions
                movedown = True
                moveup = False
        if movedown == True: # if moving down
            ymove += speedy # add speed of y
            if ymove >= 460: # if it reaches boundary switch movement
                movedown = False
                moveup = True
        # Rectangles for collisions
        collisionrect = pygame.Rect(xmove-40,ymove-10,33,70)        
        boxrect = pygame.Rect(xmove,ymove,60,60)
        pygame.draw.rect(screen,(162,116,80),boxrect)
        if xmove >= 740: # if it reaches boundary switch movement
            moveright = False
            moveleft = True
    elif moveleft == True: # if box is moving left
        xmove -= speed # subtract speed
        if moveup == True: # if box is moving up  
            ymove -= speedy # Subtract yspeed
            if ymove <= 240: # if it reaches boundary change positions
                movedown = True
                moveup = False
        if movedown == True:  # if moving down
            ymove += speedy # add speed of y
            if ymove >= 460: # if it reaches boundary switch movement
                movedown = False
                moveup = True 
         # Rectangles for collisions
        collisionRect = pygame.Rect(xmove-40,ymove,33,60)
        boxrect = pygame.Rect(xmove,ymove,60,60)        
        pygame.draw.rect(screen,(162,116,80),boxrect)
        if xmove <= 120:
            moveleft = False
            moveright = True
            
# Function that draws forklift           
def forklift ():
    global forklifthandle
    forklifthandle = pygame.Rect(xmove,ymove+70,60,40) # Rectangle for collisions
    pygame.draw.rect(screen,(247,224,29),pygame.Rect(xmove+100,420,220,140)) # forklift body
    pygame.draw.rect(screen,BLACK,pygame.Rect(xmove+240,370,80,50)) # forklift body
    pygame.draw.circle(screen,BLACK, (xmove + 160,560),40) # forklift left wheel
    pygame.draw.circle(screen,BLACK, (xmove + 260,560),40) # forklift right wheel
    pygame.draw.circle(screen,(149,160,163), (xmove + 260,560),15,5) # forklift leftwheel parts
    pygame.draw.circle(screen,(149,160,163), (xmove + 160,560),15,5) # forklift right wheel parts
    pygame.draw.line(screen,BLACK,(xmove + 110,420),(xmove + 150,300),20) # forklift roof
    pygame.draw.line(screen,BLACK,(xmove + 229,419),(xmove + 229,300),20) # forklift roof
    pygame.draw.line(screen,BLACK,(xmove + 141,309),(xmove + 239,309),20) # forklift roof
    pygame.draw.rect(screen,BLACK,pygame.Rect(xmove +85,300,15,240)) # forklift pulley
    pygame.draw.rect(screen,BLACK,pygame.Rect(xmove - 15,ymove + 60,100,20)) # forklift handle
      
    
# Function that does gamemode 1
def gamemode1 ():
    global mb,click,run,clickx,clicky,cdx,cdy,mx,my,objectx,objecty,x,y,vi,clickhistory,objectclick,xpos,ypos,collision1,collision2,goal,xmove,score,speed,end,speedy,moveup,scorey,boxrect,objectrect,xaim,yaim,noclick,collisionrect,ballmove,forklifthandle,lives,lose,repeat,collision3,dead
    if dead == False:     # if game not over
        if end == False: # if restart aim is false
            if mb == 1: # if mouse is clicked
                if click == True and run == True: # if clicks is true
                    clickx = mx # store mousex position
                    clicky = my # store mousey position
                    click = False # click is false                      
                if run == True: # if gamemode still running
                    ballmove = False # ball not moving
                    for move in range (len(objectx)): # loop for aiming
                        cdx = mx - clickx # difference between mouse and mb position
                        cdy = clicky - my # difference between mouse and mb position
                        objectx[move] = (800 - cdx) * 0.06 # factor x multiplied by to get parabola
                        objecty[move] = my * 0.0019  # factor y multiplied by to get parabola
                        if randomobject == 1: # if object is the first one
                            screen.blit(mobilePic,pygame.Rect(90,385,20,30)) # draws a mobile phone
                        if randomobject == 2: # if object is the second one
                            screen.blit(monitorPic,pygame.Rect(90,385,20,30)) # draws a monitor
                        for dots in range (30): # loop that draws parabola to aim
                            pygame.draw.circle(screen, BLACK, (xaim,yaim), 5) # circles for parabola
                            xaim += math.floor(objectx[move]) # adds x position
                            yaim -= int((vi* objecty[move])) # lowers y position
                            vi -= 10    # velocity decreases
                            run = False # run mode is false
            clickhistory = 1 # clicked once
        if clickhistory == 1 and noclick == True :
            if objectclick == True:
                xpos = mx # store x value
                ypos = my # store y value
                objectclick = False
            for move in range(len(objectx)): # loop for shooting
                if collision1 == False: # if object not colliding
                    end = True # restart disabled
                    cdx = xpos - clickx # difference between mouse and mb position
                    cdy = clicky - ypos # difference between mouse and mb position            
                    objectx[move] = (800 - cdx) * 0.06 # factor x multiplied by to get parabola
                    objecty[move] = ypos * 0.0019 # factor y multiplied by to get parabola
                    objectrect = pygame.Rect(x,y,20,30) # Rectangle for object thrown                                                    
                    if randomobject == 1 and noclick == True:  # if object is the first one
                        screen.blit(mobilePic,objectrect) # draws a mobile phone
                    elif randomobject == 2 and noclick == True: # if object is the second one
                        screen.blit(monitorPic,objectrect) # draws a monitor
                    x += math.floor(objectx[move]) # adds x position
                    y -= int((vi* objecty[move])) # lowers y position
                    vi -= 10 # velocity decreases
                    if y >= 900 or x >= 800: # if object below screen
                        noclick = False                    
                        end = False # Restart enabled
                if ((700) - (y +30)) <= ((y + 30) - (y)) and y < 800: # if object is under screen
                    lose = True # lives is lost
                    if lose == True:
                        lives -= 1 # lose 1 life
                        y = 5000 # reset y
                        lose = False                    
                if ((xmove) - (x + 20)) <= ((x + 20) - (x)) and x < xmove: # if object collides with side
                    if y > (ymove-30) and y < (ymove + 80):
                        collision1 = True
                if objectrect.colliderect(forklifthandle) and noclick == True: # if object collides with bottom
                    end = False
                    collision3 = True
                if objectrect.colliderect(boxrect) and noclick == True: # if object goes in box
                    end = False
                    collision2 = True
                    clickhistory = 0
                    
                if collision1 == True: # if object collides with side
                    for fall in range (10): # draws ball falling animation
                        x -= 2 # x decreases
                        y += 2  # y increases                 
                        if randomobject == 1: # if object is the first one
                            screen.blit(mobilePic,pygame.Rect(x,y,20,30)) # draws a mobile phone
                        elif randomobject == 2: # if object is the second one
                            screen.blit(monitorPic,pygame.Rect(x,y,20,30)) # draws a monitor
                        if y > 700: # restart if y is under screen
                            end = False
                elif collision2 == True: # if goal
                    collision2 = False
                    x += 10000 # reset x
                    y += 5000
                    goal = True # set goal to true
                    end = False
                elif collision3 == True: # if forklift collision is true
                    for fall in range (50): # draw falling animation
                        y += 2
                        x -= 0.01
                        if randomobject == 1:  # if object is the first one
                            screen.blit(mobilePic,objectrect) # draws a mobile phone
                        elif randomobject == 2: # if object is the second one
                            screen.blit(monitorPic,objectrect) # draws a monitor
                    collision3 = False
                if goal == True: # if goal is true
                    goal = False
                    for win in range(10): # output goal
                        textscore = fontback.render("Goal!" , 1, RED)
                        screen.blit(textscore, pygame.Rect(350,250,50,50))
                        pygame.display.flip()
                        if win < 9:
                            pygame.time.delay(60)
                    score += 1 # add 1 to score
                    if score % 5 == 0: # If score is multiples of 5
                        speed += 1 # increase speed
                    if score == 10:
                        moveup = True
                        scorey = True
                    if scorey == True:
                        if score % 2 == 0:
                            speedy += 1

                if lives == 0:
                    dead = True
    if dead == True: # Losing Screen
        screen.fill(GREEN)
        textlose = fontback.render("You Lost!" , 1, RED)
        screen.blit(textlose, pygame.Rect(300,50,100,50))        
        textscore = fontback.render("Score: %i" % (score) , 1, RED)
        screen.blit(textscore, pygame.Rect(300,250,100,50))
        if score <= scorehistory[0]: # Outputs High Score
            texthighscore = fontback.render("High Score: %i" % (scorehistory[0]) , 1, RED)
            screen.blit(texthighscore, pygame.Rect(300,350,100,50))
        if score > scorehistory[0]:
            texthighscore = fontback.render("High Score: %i" % (score) , 1, RED)
            screen.blit(texthighscore, pygame.Rect(300,350,100,50))        
                    
# Function for 2nd Gamemode - Time Attack                        
def gamemode2 ():
    global mb,click,run,clickx,clicky,cdx,cdy,mx,my,objectx,objecty,x,y,vi,clickhistory,objectclick,xpos,ypos,collision1,collision2,goal,xmove,score,speed,end,speedy,moveup,scorey,boxrect,objectrect,xaim,yaim,noclick,collisionrect,ballmove,forklifthandle,repeat,collision3,time,timer,count,xmove,ymove,truckx
    timer += 1000 # Timer
    if timer >= 3000:
        time = True # Stops program
        screen.fill(GREEN)
        pygame.display.flip()
        if score > int(scorehistory2[0]): # Writes high scores in text file
            numFile2 = open("score2.txt", "w")
            numFile2.write(str(score))
            numFile2.close()
        # Outputs scores and highscores
        textscore = fontback.render("Score: %i" % (score) , 1, RED)
        screen.blit(textscore, pygame.Rect(300,250,100,50))
        if score <= scorehistory2[0]:
            texthighscore = fontback.render("High Score: %i" % (scorehistory2[0]) , 1, RED)
            screen.blit(texthighscore, pygame.Rect(300,350,100,50))
        if score > scorehistory2[0]:
            scorehistory2[0] = score
            texthighscore = fontback.render("High Score: %i" % (score) , 1, RED)
            screen.blit(texthighscore, pygame.Rect(300,350,100,50))
    if time == False:
        # Outputs countdown Timer
        textcountdown = fontback.render("Time: %i" % (count) , 1, RED)
        screen.blit(textcountdown, pygame.Rect(550,100,100,50))    
        count -= 1        
        if end == False: # if restart aim is false
            if mb == 1: # if mouse is clicked
                if click == True and run == True: # if clicks is true
                    clickx = mx # store mousex position
                    clicky = my # store mousey position
                    click = False # click is false                          
                if run == True: # if gamemode still running
                    ballmove = False # ball not moving
                    for move in range (len(objectx)): # loop for aiming
                        cdx = mx - clickx  # difference between mouse and mb position
                        cdy = clicky - my # difference between mouse and mb position
                        objectx[move] = (800 - cdx) * 0.06 # factor x multiplied by to get parabola
                        objecty[move] = my * 0.0019 # factor y multiplied by to get parabola
                        if randomobject == 1: # if object is the first one
                            screen.blit(mobilePic,pygame.Rect(90,385,20,30)) # draws a mobile phone
                        if randomobject == 2: # if object is the second one
                            screen.blit(monitorPic,pygame.Rect(90,385,20,30)) # draws a monitor
                        for dots in range (30): # loop that draws parabola to aim
                            pygame.draw.circle(screen, BLACK, (xaim,yaim), 5) # circles for parabola
                            xaim += math.floor(objectx[move]) # adds x position
                            yaim -= int((vi* objecty[move])) # lowers y position
                            vi -= 10  # velocity decreases  
                            run = False # running aim is false
            clickhistory = 1
        if clickhistory == 1 and noclick == True :
            if objectclick == True: # if mouse was clicked
                xpos = mx # store x value
                ypos = my # store y value
                objectclick = False
            for move in range(len(objectx)): # Loop for shooting ball 
                if collision1 == False: # if object not colliding
                    end = True # restart disabled
                    cdx = xpos - clickx # difference between mouse and mb position
                    cdy = clicky - ypos # difference between mouse and mb position           
                    objectx[move] = (800 - cdx) * 0.06 # factor x multiplied by to get parabola
                    objecty[move] = ypos * 0.0019 # factor y multiplied by to get parabola
                    objectrect = pygame.Rect(x,y,20,30) # Rectangle for object thrown                                                    
                    if randomobject == 1 and noclick == True: # if object is the first one
                        screen.blit(mobilePic,objectrect) # draws a mobile phone
                    elif randomobject == 2 and noclick == True: # if object is the second one
                        screen.blit(monitorPic,objectrect) # draws a monitor
                    x += math.floor(objectx[move]) # increases x position
                    y -= int((vi* objecty[move])) # decreases y position
                    vi -= 10 # Velocity decreases
                    if y >= 600 or x >= 800: # if object out of screen, enable restart
                        noclick = False                    
                        end = False
                if ((xmove) - (x + 20)) <= ((x + 20) - (x)) and x < xmove: # if object collides with side of box
                    if y > (ymove-30) and y < (ymove + 80):
                        end = False  
                        collision1 = True
                if objectrect.colliderect(forklifthandle) and noclick == True: # if object collides with bottom of box
                    end = False
                    collision3 = True
                if objectrect.colliderect(boxrect) and noclick == True: # if object collides with box and is a goal
                    end = False
                    collision2 = True
                    clickhistory = 0
                    
                if collision1 == True: # if side collision = True
                    for fall in range (10): # Side collision falling animation
                        x -= 2
                        y += 2                    
                        if randomobject == 1: # if first object
                            screen.blit(mobilePic,pygame.Rect(x,y,20,30)) # mobile phone drawn
                        elif randomobject == 2: # if second object
                            screen.blit(monitorPic,pygame.Rect(x,y,20,30)) # monitor Drawn
                elif collision2 == True: # if collision from top
                    collision2 = False
                    x += 900 # reset x
                    goal = True # goal is true
                    end = False
                elif collision3 == True: # if collision from bottom
                    for fall in range (50): # animation for falling
                        y += 2
                        x -= 0.01
                        if randomobject == 1: # if first object
                            screen.blit(mobilePic,objectrect) # mobile phone drawn
                        elif randomobject == 2: # if second object
                            screen.blit(monitorPic,objectrect) # monitor Drawn
                    collision3 = False
                if goal == True: # if goal is true
                    goal = False
                    score += 1 # add 1 to score
                    if score % 5 == 0:
                        speed += 1 # increase speed every multiple of 5
                    if score == 10: # start moving up and down
                        moveup = True
                        scorey = True
                    if scorey == True:
                        if score % 5 == 0: # increase speed of y direction
                            speedy += 1
                    
# A function that reets all variables
def reset ():
    global vi,y,x,run,clickx,clicky,cdx,cdy,objectclick,collision1,collision2,collisin3,end,mousehistory,xaim,yaim
    if mb == 1 and run == False: # if mouse is clicked again 
        # Reset all the following Variables
        y = 385
        x = 90
        xaim = 100
        yaim = 400        
        vi = 100
        clickx = 0
        clicky = 0
        cdx = 0
        cdy = 0
        objectclick = True
        collision1 = False
        collision2 = False
        end = False
        collision3 = False
        run = True
        
# Defining function for menu 
def menu():
    global mousehistory, mb, mx, my, menuopt, running, menurun,escape,score,gamemap,gamemode,clickchange,change,mode1,mode2,lives,playstart,playgame,count,time # making all variables global
    # Starts program and plays music
    if mousehistory == 0:
        if menurun == 0 and mousehistory == 0:
            menuSound.play() # menu music
            menurun = 1
        screen.blit(menuPic, pygame.Rect(0,0,800,600)) # menu background
        # Draws the 3 options in menu
        texttitle = fonttitle.render("E-Hoops" , 1, (r,g,b)) # title text
        screen.blit(texttitle, title)        
        text1 = fontmenu.render("Play" , 1, GREEN) # first option text
        screen.blit(text1, indicator)
        text2 = fontmenu.render("How to Play" , 1, GREEN) # second option Text
        screen.blit(text2, indicator2)        
        text3 = fontmenu.render("Quit" , 1, GREEN) # Third option text
        screen.blit(text3, indicator3)
        # Makes a mouse over effect on first option and tells it what to do when mouse is clicked
        if indicator.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:
                text1 = fontmenu.render("Play" , 1, RED)
                screen.blit(text1, indicator)
            if mb == 1: # if mouse is clicked
                mousehistory = 1
                menuopt = 1 # menu option = 1
                escape = False
                # Stops menu music
                pygame.mixer.stop()            
                menurun = 0
        # Makes a mouse over effect on second option and tells it what to do when mouse is clicked
        if indicator2.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:            
                text2 = fontmenu.render("How to Play" , 1, RED)
                screen.blit(text2, indicator2)
            if mb == 1: # if mouse is clicked              
                mousehistory = 1
                menuopt = 2 # menu option is 2
                escape = False
                menurun = 0
                
        # Makes a mouse over effect on third option and tells it what to do when mouse is clicked        
        if indicator3.collidepoint(mx,my) and mousehistory == 0:
            if mb == 0:
                text3 = fontmenu.render("Quit" , 1, RED)
                screen.blit(text3, indicator3)
            if mb == 1: # if mouse is clicked
                mousehistory = 1
                menuopt = 3 # menuoption is 3
                # Stops menu music
                pygame.mixer.stop()            
                menurun = 0
    # If Mouse is clicked the following happens
    if mousehistory == 1:
        if menuopt == 1 and mousehistory == 1: # if menu option is 1
            # Gamemode menu starts
            if playstart == 0:
                screen.fill(BLUE)
                textmaptitle = fontmode.render("Map", 1, ORANGE) # title 
                screen.blit(textmaptitle, pygame.Rect(360,30,30,20))                
                pygame.draw.rect(screen,ORANGE,pygame.Rect(300,100,200,100)) # map change
                pygame.draw.polygon(screen, (255,255,255), [[520,125], [550, 150],[520,175]]) # arrow
                pygame.draw.polygon(screen, (255,255,255), [[280,125], [250, 150],[280,175]]) # arrow
                textmodetitle = fontmode.render("Mode", 1, ORANGE) # title 2
                screen.blit(textmodetitle, pygame.Rect(360,330,30,20))                  
                pygame.draw.rect(screen,ORANGE,pygame.Rect(300,400,200,100)) # modechange            
                pygame.draw.polygon(screen, (255,255,255), [[520,425], [550, 450],[520,475]]) # arrow
                pygame.draw.polygon(screen, (255,255,255), [[280,425], [250, 450],[280,475]]) # arrow
                if mapchangeright.collidepoint(mx,my) and mb == 1 and change == False: # if map change right arrow is clicked
                    gamemap += 1 # Game map changes
                    change = True
                elif mapchangeleft.collidepoint(mx,my) and mb ==1 and change == False: # if map change left arrow is clicked
                    gamemap -= 1 # Game map changes
                    change = True
                if modechangeright.collidepoint(mx,my) and mb == 1 and change == False: # if mode change left arrow is clicked
                    gamemode += 1 # gamemode changes
                    change = True
                elif modechangeleft.collidepoint(mx,my) and mb == 1 and change == False: # if mode change right arrow is clicked
                    gamemode -= 1 # gamemode changes
                    change = True
                if mb == 0: 
                    change = False # cannot hold mouseclick
                if gamemap == 3: # resets map
                    gamemap = 0
                if gamemap == -1: # resets map
                    gamemap = 2
                if gamemode == 2: # resets mode
                    gamemode = 0
                if gamemode == -1: # resets mode
                    gamemode = 1
                if gamemode == 0: # text for first mode
                    textmode = fontmode.render("Normal", 1, BLACK)
                    screen.blit(textmode, pygame.Rect(340,430,460,60))
                if gamemode == 1: # text for second mode
                    textmode = fontmode.render("Time Attack", 1, BLACK)
                    screen.blit(textmode, pygame.Rect(315,430,460,60))
                if gamemap == 0: # pic for first map
                    screen.blit(background1menuPic, pygame.Rect(310,110,180,80))
                if gamemap == 1: # pic for second map
                    screen.blit(background2menuPic, pygame.Rect(310,110,180,80))
                if gamemap == 2: # pic for third map
                    screen.blit(background3menuPic, pygame.Rect(310,110,180,80))
                # Play button
                textplay = fontmode.render("Play", 1, GREEN)
                screen.blit(textplay,play)
            if play.collidepoint(mx,my):
                if mb == 0: # changes colour when mouse hovers over it
                    textplay = fontmode.render("Play", 1, RED)
                    screen.blit(textplay,play)
                    playgame = True
                if mb == 1 and playgame == True: # if mouse is clicked
                    playgame = False
                    #chack what gamemode is chosen
                    if gamemode == 0: 
                        mode1 = True
                        playstart = 1
                    if gamemode == 1:
                        mode2 = True
                        playstart = 1
                   
            if mode1 == True: # if gammode is 1
                if menurun == 0: # play music
                    mode1Sound.play()                    
                if gamemap == 0: # chack which map is chosen and display it
                    screen.blit(background1Pic, pygame.Rect(0,0,800,600))
                elif gamemap == 1:
                    screen.blit(background2Pic, pygame.Rect(0,0,800,600))
                elif gamemap == 2:
                    screen.blit(background3Pic, pygame.Rect(0,0,800,600))
                # display score, highscore and lives
                textscore = fontback.render("Score: %i" % (score) , 1, GREEN)
                screen.blit(textscore, back)
                textscore = fontback.render("Lives: %i" % (lives) , 1, GREEN)
                screen.blit(textscore, pygame.Rect(600,140,100,100))                
                if score <= scorehistory[0]:
                    texthighscore = fontback.render("High Score: %i" % (scorehistory[0]) , 1, GREEN)
                    screen.blit(texthighscore, pygame.Rect(20,20,100,50))
                if score > scorehistory[0]:
                    scorehistory[0] = score                    
                    texthighscore = fontback.render("High Score: %i" % (score) , 1, GREEN)
                    screen.blit(texthighscore, pygame.Rect(20,20,100,50))
                # call all functions needed
                forklift()
                boxmove ()
                gamemode1()             
                reset()
             
                menurun += 1                                                 
            if mode2 == True: # if gamemode is 2
                if menurun == 0: # play music
                    mode2Sound.play()                  
                if gamemap == 0: # check which map is chosen and display it
                    screen.blit(background1Pic, pygame.Rect(0,0,800,600))
                elif gamemap == 1:
                    screen.blit(background2Pic, pygame.Rect(0,0,800,600))
                elif gamemap == 2:
                    screen.blit(background3Pic, pygame.Rect(0,0,800,600))
                # Display's scores and highscores
                textscore = fontback.render("Score: %i" % (score) , 1, GREEN)
                screen.blit(textscore, back)
                if score <= scorehistory2[0]:
                    texthighscore = fontback.render("High Score: %i" % (scorehistory2[0]) , 1, GREEN)
                    screen.blit(texthighscore, pygame.Rect(20,20,100,50))
                if score > scorehistory2[0]:
                    texthighscore = fontback.render("High Score: %i" % (score) , 1, GREEN)
                    screen.blit(texthighscore, pygame.Rect(20,20,100,50))
                # calls all functions necesarry to run the mode
                forklift()
                boxmove ()
                gamemode2()        
                reset()             
                menurun += 1                                 
            # Mouse over effect on back button and goes back to menu when clicked
            if escape == True: # if esc is clicked 
                # records highscores
                if score > int(scorehistory[0]):
                    numFile = open("score.txt", "w")
                    numFile.write(str(score))
                    numFile.close()
                # resets everything
                screen.fill(BLACK)
                score = 0                
                mousehistory = 0
                menurun = 0
                # Stops sounds
                pygame.mixer.stop()
        # Menu option 2 content
        if menuopt == 2 and mousehistory == 1:
            screen.blit(controlsPic, pygame.Rect(0,0,800,600))
            menurun += 1
            # Mouse over effect on back button and goes back to menu when clicked
            if escape == True:
                screen.fill(BLACK)
                mousehistory = 0  
                menurun = 0
                pygame.mixer.stop()
        # Quits program when option 3 is selected
        if menuopt == 3 and mousehistory == 1:            
            running = False

while running:
    # Closes program when x is clicked
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            # Opens text file
            # records highscores
            if score > int(scorehistory[0]):
                numFile = open("score.txt", "w")
                numFile.write(str(score))
                numFile.close()            
            running = False
        # if key is pressed
        if evnt.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed() 
            # if escape is pressed
            if key[pygame.K_ESCAPE] and menuopt == 1:
                # reset all the following variables and return to mainmenu
                escape = True
                mode1 = False
                mode2 = False
                gamemode = 0
                gamemap = 1
                playstart = 0
                timer = 0
                time = False
                dead = False
                lives = 11
                moveup = False
                movedown = False
                ymove = 400
                speedy = 1
                speed = 1
                reset()
            elif key[pygame.K_ESCAPE] and menuopt == 2:
                escape = True
                reset()
    colour += 1 # changes colour
    if colour % 10 == 0: # random colours for title
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        
    mx, my, mb = getmouse()
    if mb == 0:
        noclick = True
        
    menu()
    
    pygame.display.flip()
    
    # 30 FPS
    myClock.tick(30)
# Quits program when done
pygame.quit()        