import pyglet
import random
from pyglet.window import key
from pyglet import shapes
from random import randint
import pygetwindow as wp
from platforms import Platform
import pyautogui
import time

x = 500
y = 0
velX = 0
velY = 0
grounded = False
floorHeight = 850
Gravity = 2
onPlatform = False
fallingSpeed = 1
score = 0
scoreTime_start = time.time()
scoreTime_end = time.time()

scoreWindow = pyglet.window.Window(width=300,height=100,caption='SCORE')
scoreLabel = pyglet.text.Label('Score: '+str(score), font_name='Times New Roman', font_size=24, x=scoreWindow.width//2, y=scoreWindow.height//2,anchor_x='center', anchor_y='center')
@scoreWindow.event
def on_draw():
    global score,scoreTime_start,scoreTime_end
    scoreWindow.clear()
    scoreLabel.draw()
    scoreTime_end = time.time()
    if scoreTime_end - scoreTime_start >= 1:
        scoreTime_start = time.time()
        score += 1
    

            

platformesList = [Platform(x + 250,y + 500,500,100)]

def UPDATE():
    global x, y, velX, velY,Gravity,grounded,floorHeight,onPlatform,fallingSpeed
    
    if y >= floorHeight:
        velY = 0
        grounded = True
    else: grounded = False


    if grounded == False:
        velY += Gravity

    x += velX
    y += velY

    if y > 850:
        MainWindow.close()
        for platforms in platformesList:
            platforms.GameWindow.close()
    

    floorHeight = 850
    #PLATFORMS
    platformWindowlist = wp.getWindowsWithTitle("PLATFORM")
    for i in range(len(platformesList)):
        platformesList[i].update()
        
        if x + 600 > platformesList[i].x and x < platformesList[i].x + platformesList[i].width - 500: #GAMBIARRA
            if y < platformesList[i].y + platformesList[i].height:
                floorHeight = platformesList[i].y - platformesList[i].height
                onPlatform = True
        else: onPlatform = False
        

        platformWindowlist[i].moveTo(platformesList[i].x,platformesList[i].y)
        platformesList[i].y += int(fallingSpeed)
        fallingSpeed += 0.01
        

    

        

    
    playerWindow.moveTo(int(x + 500),int(y))
    

running = True

MainWindow = pyglet.window.Window(width=100,height=100,caption='PLAYER')
background = pyglet.shapes.Rectangle(0,0,100,100,color=(255,0,0))



@MainWindow.event
def on_draw():
    MainWindow.clear()
    background.draw()
    UPDATE()



@MainWindow.event
def on_key_press(symbol,modifier):
    global velX, velY, x, y,running,grounded,Jumped,Gravity
    if symbol == key.A:
        velX = -10
        
    elif symbol == key.D:
        velX = 10


    elif symbol == key.W and grounded == True:
        y -= 50
        velY = -40
        Jumped = True
        grounded = False

    elif symbol == key.R:
        if len(platformesList) == 0:
            platformesList.append(Platform(pyautogui.position().x - 250,pyautogui.position().y,500,100))

        else:
            platformesList[0].GameWindow.close()
            platformesList[0] = Platform(pyautogui.position().x - 250,pyautogui.position().y,500,100)

        




@MainWindow.event
def on_key_release(symbol,modifier):
    global velX, velY, x, y,running
    if symbol == key.A or symbol == key.D:
        velX = 0
        


        
        
playerWindow = wp.getWindowsWithTitle('PLAYER')[0]

while running:
    pyglet.app.run()

