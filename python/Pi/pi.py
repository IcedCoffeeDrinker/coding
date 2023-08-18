from tkinter import *
from math import *
import round_canvas as round
import random

#settings
speed = 1 # in ms
window_width = 1000 # not changable -- random point rounded
window_height = floor(window_width / 16 * 10)
cell = window_width / 32
font = "Helvetica"
color = "black"

#window
win = Tk()
win.title("Pi")
win.resizable(False, False)
win.geometry(str(window_width) + "x" + str(window_height))
win.configure(background="#2D3436")

# variabes
radius = (cell*18-50-10)/2
simuCenter = cell*10 # relative to total window
simuCanvasCenter = cell*9-25 # relative to simulation canvas
pointsInCircle = 0
pointsTotal = 0
Pi = 0
realPi = 3.14159265359 # to calculate difference

# functions
def activate():
    start.destroy()
    main()

def randomPoint():
    rr = radius*2 # radius from .25 to .0 to .5
    value = random.random()
    #print(value)
    xy = value * rr + 5
    return xy

def inCircle(x, y):
    global pointsInCircle
    global pointsTotal
    relCenterX = x - simuCanvasCenter
    relCenterY = y - simuCanvasCenter
    distance = sqrt(relCenterX*relCenterX + relCenterY*relCenterY)

    if distance <= radius: # ???
        pointsInCircle += 1
        pointsTotal += 1
        return True
    else:
        pointsTotal += 1
        return False

# main
def main():
    # 1. set random point
    x = randomPoint()
    y = randomPoint()

    # 2. check if in in circle
    inCircle_val = inCircle(x, y)

    # 3. draw point
    if inCircle_val == True:
        point = simuCanvas.create_oval(x, y, x+1, y+1, outline="aqua", width=1)
    else:
        point = simuCanvas.create_oval(x, y, x+1, y+1, outline="violetred1", width=1)

    # 4. (re)calculate pi
    global Pi
    Pi = 4 * (pointsInCircle / pointsTotal)

    printPi.config(text=Pi)
    printPointsIn.config(text=pointsInCircle)
    printPointsOut.config(text=pointsTotal)
    # calculate difference
    difference = str(abs(Pi-realPi))
    printDifference.config(text="+ -  " + difference)

    win.after(speed, main)



# display setup
canvas = Canvas(win, width=window_width, height=window_height, bg="#2D3436", highlightthickness=0)
canvas.place(x=0,y=0)
canvas_overlay = round.round_rectangle(canvas, cell, cell, cell*(18+1), cell*(18+1), radius=20, fill="#636E72")
pi_overlay = round.round_rectangle(canvas, cell*20, cell, cell*(11+20), cell*(5+1)-10, radius=20, fill="#636E72")

simuCanvas = Canvas(win, width=cell*18-50, height=cell*18-50, highlightthickness=0, bg="#636E72")
simuCanvas.place(x=cell+25,y=cell+25)

piCanvas = Canvas(win, width=cell*11-50, height=cell*5-50-10, highlightthickness=0, bg="#636E72")
piCanvas.place(x=cell*20+25,y=cell+25)

# start button
start = Button(win, text="start", command=activate, font=(font, 16), fg=color)
start.place(x=simuCenter,y=simuCenter,anchor=CENTER)

# statistics
printPi = Label(piCanvas, text=Pi, font=(font, 16), fg="#CFCFCF", bg="#636E72", anchor="w")
printPi.pack(fill='both')
printDifference = Label(piCanvas, text="+ -  x", font=(font, 16), fg="#ED4D4D", bg="#636E72", anchor="w")
printDifference.pack(fill='both')
printPointsIn = Label(piCanvas, text=pointsInCircle, font=(font, 16), fg="aqua", bg="#636E72", anchor="w")
printPointsIn.pack(fill='both')
printPointsOut = Label(piCanvas, text=pointsTotal, font=(font, 16), fg="violetred1", bg="#636E72", anchor="w")
printPointsOut.pack(fill='both')

# draw map
simuCanvas.create_rectangle(5, 5, radius*2+5, radius*2+5, outline="#B2BEC3", width=1)
simuCanvas.create_oval(5, 5, radius*2+5, radius*2+5, outline="#B2BEC3", width=1)
simuCanvas.create_oval(simuCanvasCenter-2, simuCanvasCenter-2, simuCanvasCenter+2, simuCanvasCenter+2, outline="#B2BEC3", width=5, fill="#B2BEC3")

win.mainloop()
