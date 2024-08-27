import pyglet
from pyglet.window import key
from pyglet import shapes
import random
import pygetwindow as wp
import keyboard as ky

x = 0
y = 0
velX = 0
velY = 0

running = True
MainWindow = pyglet.window.Window(width=100,height=100,caption='PLAYER')
SecondWindow = pyglet.window.Window(width=100,height=100,caption='PLAYER')

playerWindow = wp.getWindowsWithTitle('PLAYER')[0]
secondWindow = wp.getWindowsWithTitle('PLAYER')[1]

def UPDATE():
    global x, y, velX, velY
    x += velX
    y += velY

while running:
    playerWindow.moveTo(int(x + 100),int(y))
    secondWindow.moveTo(-x,y)
    UPDATE()
    if ky.is_pressed('d'):
        velX = 1

    if ky.is_pressed('a'):
        velX = -1

    if ky.is_pressed('f'):
        running = False
    
