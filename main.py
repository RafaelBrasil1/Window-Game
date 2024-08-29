from tkinter.ttk import Style
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
menu = True
running = True

if menu == True:
    PlayWindow = pyglet.window.Window(width=300,height=100,caption='PLAY')
    PlayLabel = pyglet.text.Label('PLAY', font_name='Times New Roman', font_size=24, x=PlayWindow.width//2, y=PlayWindow.height//2,anchor_x='center', anchor_y='center')
    playGetWindow = wp.getWindowsWithTitle("PLAY")[0]

    @PlayWindow.event
    def on_draw():
        PlayWindow.clear()
        PlayLabel.draw()
        playGetWindow.moveTo(800,200)

    @PlayWindow.event
    def on_mouse_press(x, y, button, modifiers):
        global menu
        menu = False
        PlayWindow.close()
        HowToPlayWindow.close()
        Game()

    HowToPlayWindow = pyglet.window.Window(width=300,height=100,caption='HOW TO PLAY')
    howToPlayLabel = pyglet.text.Label('HOW TO PLAY', font_name='Times New Roman', font_size=24, x=HowToPlayWindow.width//2, y=HowToPlayWindow.height//2,anchor_x='center', anchor_y='center')
    HowToGetWindow = wp.getWindowsWithTitle("HOW TO PLAY")[0]


    Info = pyglet.window.Window(width=500,height=500,caption='INFORMATION')
    InfoLabel = pyglet.text.Label('Dont let the red window fall on the floor', font_name='Times New Roman', font_size=20, x=Info.width//2, y=Info.height//1.2,anchor_x='center', anchor_y='center')
    InfoLabel2 = pyglet.text.Label('Use "R" to create platforms on', font_name='Times New Roman', font_size=20, x=Info.width//2, y=Info.height//2,anchor_x='center', anchor_y='center')
    InfoLabel3 = pyglet.text.Label('your mouse position', font_name='Times New Roman', font_size=20, x=Info.width//2, y=Info.height//2.3,anchor_x='center', anchor_y='center')
    infoWindow = wp.getWindowsWithTitle('INFORMATION')[0]
    Info.set_visible(False)

    

    @Info.event
    def on_draw():
        Info.clear()
        InfoLabel.draw()
        InfoLabel2.draw()
        InfoLabel3.draw()
        infoWindow.moveTo(700,200)


    @Info.event
    def on_close():
        PlayWindow.set_visible(True)


    @HowToPlayWindow.event
    def on_draw():
        HowToPlayWindow.clear()
        howToPlayLabel.draw()
        HowToGetWindow.moveTo(800,600)

    @HowToPlayWindow.event
    def on_mouse_press(x, y, button, modifiers):
        Info.set_visible(True)
        HowToPlayWindow.set_visible(False)
        PlayWindow.set_visible(False)



def Game():                

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
        

    

    MainWindow = pyglet.window.Window(width=100,height=100,caption='PLAYER')
    background = pyglet.shapes.Rectangle(0,0,200,200,color=(255,0,0))



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

