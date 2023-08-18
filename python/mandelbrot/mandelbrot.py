from tkinter import *
from math import *
from color import *
from tqdm import tqdm

print("import finished")

# settings
window_width = 2160 # wtf what ever??!!
resolution = float(input("Enter resolution: ")) # 1 = 100%  2 = 200%
max_eturations = int(input("Enter accuracy: ")) # 200 normal (accuracy)
outside_radius = 2
pixel_size = 1/resolution

win = Tk()
win.title("Mandelbrot")
win.attributes("-fullscreen", True)
win.configure(background="#212529")

# variables
window_height = window_width/16*9
canvas_size = window_height
cords = []
offsetX = (window_width-canvas_size)/2

# functions
def calculate(Cr,Ci): # input is C (real + imaginary)
    Z = [0,0]
    for eturation in range(max_eturations):
        r = Z[0]
        i = Z[1]
        localA = r**2 + i**2 *-1 +Cr # square complex numbers :)
        localB = r*i *2 +Ci
        Z = [localA,localB]
        if sqrt(localA*localA+localB*localB) > 2:
            return color(eturation,max_eturations,"hex")
    if sqrt(localA*localA+localB*localB) <= 2:
        return True

def draw(x,y,color):
    canvas.create_rectangle(x, y, x+pixel_size, y+pixel_size, fill=color, width=0)

def process():
    for y in tqdm(range(int(resolution*canvas_size))):
        cords.append([])
        for x in range(int(resolution*canvas_size)):
            a = 4/(resolution*canvas_size)*x-2 # convert x,y to complex plane
            b = 4/(resolution*canvas_size)*y-2
            inside = calculate(a,b)
            localX = x/resolution # screen cords
            localY = y/resolution
            if inside == True:
                draw(localX,localY,"black")
            else:
                color = inside
                draw(localX,localY,color)
                cords[y].append([localX,localY,inside])

# main
def main():
    print()
    global canvas
    canvas = Canvas(win, width=canvas_size, height=canvas_size, bg="white", highlightthickness=0)
    canvas.place(x=offsetX,y=0)
    print("canvas was drawn")
    process()
    print("finished")
main()
print("looping")
win.mainloop()
