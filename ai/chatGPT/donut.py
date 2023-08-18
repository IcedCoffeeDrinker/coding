import time
from tkinter import *

class Donut(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.radius = 8
        self.x = 500 / 2
        self.y = 500 / 2
        self.id = canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill="red")
    def draw(self):
        self.canvas.move(self.id, 1, 0)
        self.canvas.after(100, self.draw)

window = Tk()
canvas = Canvas(window, width=500, height=500)
canvas.pack()
donut = Donut(canvas)
donut.draw()
window.mainloop()
