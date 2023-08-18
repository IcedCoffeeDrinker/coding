from tkinter import *
from math import *
import round_canvas as round

#settings
speed = 1 # in ms
window_size = 700
cellamount = 20
cell = window_size / cellamount
r = 300
pointSize = 20
animationSize = window_size - cell*4
lineWidth = 3
factor = 2
point_amount = int(input("Enter amount of joints:\n"))

#colors:
#48979b
#7cbeba
#a7c7b3
#d9beac
#f5e6d9

#window
win = Tk()
win.title("heart")
win.resizable(False, False)
win.geometry(str(window_size) + "x" + str(window_size))
win.configure(background="#f5e6d9")

# variables
point_cords = [] # saves point rotations in list (place in list coresponds to number of point)
point_cordsXY = [] # saves point with x,y

# canvas
canvas = Canvas(win, width=window_size, height=window_size, bg="#f5e6d9", highlightthickness=0)
canvas.place(x=0,y=0)
canvas_overlay = round.round_rectangle(canvas, cell, cell, cell*cellamount-cell, cell*cellamount-cell, radius=40, fill="#d9beac")

# functions:
def drawPoints(): # calculates point angles
    for point in range(point_amount):
        #print(point)
        localPoint = 360/(point_amount)*point
        point_cords.append(localPoint)

def showPoints(): # transforms coordinates and shows point
    for angle in point_cords:
        localX = cos(radians(angle))*r+window_size/2 # https://www.youtube.com/watch?v=AWZW1OwpT-w
        localY = sin(radians(angle))*r+window_size/2
        print(angle)
        print(localX, localY)
        point_cordsXY.append([localX,localY])
        visiblePoint = canvas.create_oval(localX-pointSize/2, localY-pointSize/2, localX+pointSize/2, localY+pointSize/2, width=0, fill="#7cbeba")
    print(point_cordsXY)

def drawLine(x,y,x2,y2):
    canvas.create_line(x, y, x2, y2, fill="#48979b", width=lineWidth)

def calculateLines():
    forCounter = 0
    for point in point_cordsXY: # fors trough every point in point_cordsXY

        localX = point[0]
        localY = point[1]
        for pos in range(len(point_cordsXY)):
            if localX == point_cordsXY[pos][0] and localY == point_cordsXY[pos][1]:
                position = pos
            else:
                pos +=1

        wantedPoint = position*factor
        selectedPoint = 0
        actualPoint = selectedPoint

        while wantedPoint != selectedPoint:
            #print(wantedPoint, selectedPoint)
            actualPoint = selectedPoint
            if actualPoint >= len(point_cordsXY):
                while actualPoint >= len(point_cordsXY):
                    actualPoint -= len(point_cordsXY)
            if wantedPoint != selectedPoint:
                selectedPoint += 1

        localX2 = point_cordsXY[actualPoint][0]
        localY2 = point_cordsXY[actualPoint][1]
        drawLine(localX,localY,localX2,localY2)
        print(forCounter)
        forCounter += 1

# main
def main():
    drawPoints()
    showPoints()
    calculateLines()

win.after(speed,main)
win.mainloop()
