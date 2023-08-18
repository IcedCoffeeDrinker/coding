from tkinter import *
import time
from pynput.keyboard import *
from math import *


# settings
window_height = 700
window_width = 700

# window
win = Tk()
win.title("Rocket")
win.resizable(False, False)
win.geometry(str(window_width) + "x" + str(window_height))
win.configure(background="#000000")
can = Canvas(win,width=window_width,height=window_height,bg="#000000",highlightthickness=0)
can.place(x=0,y=0)

# other
windowPosX = 0
windowPosY = 0

# functions
class rocket:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.v = [0,0]
        self.r = 0 # 0-1
        self.shape = [-15,25, 15,25, 0,-25, -15,25]
        self.sprite = can.create_polygon(self.shape, fill="white")

        self.boosterState = False
        self.activeTurn = False

        self.cordsLabel= Label(can, text=(self.x,self.y), font=("Helvetica", 16), fg="#CFCFCF", bg="black", anchor="w")
        self.cordsLabel.place(x=0,y=0)
        self.velLabel= Label(can, text=(self.v[0],self.v[1]), font=("Helvetica", 16), fg="#CFCFCF", bg="black", anchor="w")
        self.velLabel.place(x=0,y=30)

        # control
        self.boostAdder = 0.4
        self.maxVel = 7
        self.turnAdder = 0.02
        self.vstop = 0.08

    def velocity_vector(self,velocity, angle):
        x_velocity = velocity * cos(angle)
        y_velocity = velocity * sin(angle)
        return [ y_velocity,x_velocity]

    def boost(self):
        if abs(self.v[0])+abs(self.v[1]) < self.maxVel:
            newV = self.velocity_vector(-self.boostAdder,self.r*pi*2)
            self.v[0] += newV[0]
            self.v[1] += newV[1]

    def turn(self,direction):
        if direction == "right":
            self.r -= self.turnAdder
        else:
            self.r += self.turnAdder

    def slow_down(self):
        if self.v[0] != 0 or self.v[1] != 0:
            velAngle = atan2(self.v[0],self.v[1]) # calculate angle of velocity as radiant
            newV = self.velocity_vector(-self.vstop,velAngle)
            self.v[0] += newV[0]
            self.v[1] += newV[1]
            for i in range(2):
                if abs(self.v[i]) < self.vstop:
                    self.v[i] = 0

    def update_shape(self):
        abs_shape = []
        self.x += self.v[0] # add velocity
        self.y += self.v[1]
        addX = window_width/2+self.x # add coordinates
        addY = window_height/2+self.y
        for i in range(len(self.shape)): # rotation
            angle = pi*2*self.r

            if (i % 2) == 0:
                y = self.shape[i+1]
                x = self.shape[i]
                x = x*cos(angle)+y*sin(angle)
                x += addX
                abs_shape.append(x)
            else:
                x = self.shape[i-1]
                y = self.shape[i]
                y = -x*sin(angle)+y*cos(angle)
                y += addY
                abs_shape.append(y)
        can.delete(self.sprite)
        self.sprite = can.create_polygon(abs_shape, fill="white")

    def stats(self):
        self.cordsLabel.config(text=(floor(self.x),floor(self.y)))
        self.velLabel.config(text=(self.v[0],self.v[1]))

    def update(self):
        if self.boosterState == True:
            self.boost()
        if self.activeTurn != False:
            self.turn(self.activeTurn)

        self.update_shape()
        self.slow_down()
        self.stats()

def on_press(key):
    if key == Key.up:
        main_rocket.boosterState = True
    if key == Key.right:
        main_rocket.activeTurn = "right"
    if key == Key.left:
        main_rocket.activeTurn = "left"

def on_release(key):
    if key == Key.up:
        main_rocket.boosterState = False
    else:
        main_rocket.activeTurn = False

# mian
def loop():
    while True:
        main_rocket.update()
        win.update()
        #time.sleep(0.01)

def main():
    global main_rocket
    main_rocket = rocket()
    listener = Listener(on_press=on_press,on_release=on_release)
    listener.start()
    loop()
main()

win.mainloop()
