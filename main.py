import pyglet
import random
from pyglet.window import key
from pyglet import shapes
from random import randint
import pygetwindow as wp
from platforms import Platform

x = 500
y = 0
velX = 0
velY = 0
grounded = False
floorHeight = 850
Gravity = 1

def UPDATE():
    global x, y, velX, velY,Gravity,grounded

    if y >= floorHeight:
        y = floorHeight
        grounded = True
    else: grounded = False

    if grounded == False:
        velY += Gravity

    x += velX
    y += velY


    if x + 500> myPlatform.x and x < myPlatform.x + myPlatform.width - 500: #GAMBIARRA
        if y + 100 > myPlatform.y and y < myPlatform.y + myPlatform.height:
            print("collison")

    windowPlatform.moveTo(myPlatform.x,myPlatform.y)
    playerWindow.moveTo(int(x + 500),int(y))
    

running = True

MainWindow = pyglet.window.Window(width=100,height=100,caption='PLAYER')
background = pyglet.shapes.Rectangle(0,0,100,100,color=(255,0,0))

#PLATFORMS

myPlatform = Platform(200,100,500,100)

myPlatform.update()
windowPlatform = wp.getWindowsWithTitle("PLATFORM")[0]


@MainWindow.event
def on_draw():
    MainWindow.clear()
    background.draw()
    UPDATE()



@MainWindow.event
def on_key_press(symbol,modifier):
    global velX, velY, x, y,running,grounded
    if symbol == key.A:
        print("AA")
        velX = -10
        
    elif symbol == key.D:
        print("DD")
        velX = 10


    elif symbol == key.W and grounded == True:
        print("WW")
        velY += -50
        grounded = False

    elif symbol == key.F:
        MainWindow.close()



@MainWindow.event
def on_key_release(symbol,modifier):
    global velX, velY, x, y,running
    if symbol == key.A or symbol == key.D:
        velX = 0
        

    elif symbol == key.S or symbol == key.W:
        velY = 0

        
        
playerWindow = wp.getWindowsWithTitle('PLAYER')[0]

while running:
    pyglet.app.run()

