import pyglet
import random
from pyglet.window import key
from pyglet import shapes
from random import randint
import pygetwindow as wp

class Platform():
    def __init__(self,x,y,width,height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.GameWindow = pyglet.window.Window(width=self.width,height=self.height,caption='PLATFORM')
        self.background = pyglet.shapes.Rectangle(0,0,self.width,self.height,color=(0,255,0))


    def update(self):
        @self.GameWindow.event
        def on_draw():
            self.GameWindow.clear()
            self.background.draw()
            
        





