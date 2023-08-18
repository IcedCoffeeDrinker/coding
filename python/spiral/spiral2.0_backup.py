from tkinter import *
from math import *

#settings
window_size = 800
space = window_size / 20
numbers = True
font = "Helvetica"
color = "black"
speed = 1 #ms                   -normal: 100

#window
win = Tk()
win.title("spiral lol")
win.resizable(False, False)
win.geometry(str(window_size) + "x" + str(window_size))
win.configure(background="white")


# variabes
run = False
steps = 0
digit = 1
neededSteps = 1
direction = "right"
xpo = window_size / 2
ypo = window_size / 2
colorList = ["black", "white", "blue", "red", "violetred1", "springgreen", "aqua", "aliceblue", "azure3", "crimson", "gold1"]


# start
def activate():
    global run
    run = True
    startButton.destroy()

# draw canvas
def createCanvas():
    global canvas
    canvas = Canvas(win, width=window_size, height=window_size, bg="white")
    canvas.place(x=0,y=0)
    print("canvas")

createCanvas()

# draw line
def drawLine():
    canvas.create_line(oldxpo, oldypo, xpo, ypo, fill=color, width=space/13.33) # when space=40 arround 3
    
# prime checker
def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    if num == 1:
        return False
    return True

# main
def main():
    global run
    global steps
    global digit
    global neededSteps
    global direction
    global xpo
    global ypo
    global oldxpo
    global oldypo
    
    if run == True:
        # 1. print
        if numbers == True:
            label = Label(win, text=digit, bg="white",fg=color, font=(font, 16))
            label.place(x=xpo,y=ypo)
            print("digit: ", digit, " neededSteps: ", neededSteps, " direction: ", direction)
        else:
            if isprime(digit) == True:
                canvas.create_oval(xpo-space/2.2, ypo-space/2.2, xpo+space/2.2, ypo+space/2.2, fill=color)
        
        # save old coordinates
        oldxpo = xpo
        oldypo = ypo
        
        # 2. move
        if steps < floor(neededSteps):
            if direction == "right":
                xpo += space
            elif direction == "up":
                ypo -= space
            elif direction == "left":
                xpo -= space
            elif direction == "down":
                ypo += space
            steps += 1
            digit += 1
            
        # line drawing
        if numbers == False:
            drawLine()
            
        # 3. turn
        if steps == floor(neededSteps):
            if direction == "right":
                direction = "up"
            elif direction == "up":
                direction = "left"
            elif direction == "left":
                direction = "down"
            elif direction == "down":
                direction = "right"
            steps = 0
            neededSteps += 0.5
        
        #stop drawing
        if xpo > window_size or ypo > window_size:
            run = False
        
        
    win.after(speed, main)



# start
startButton = Button(win, text="start", padx=50, pady=50, command=activate, fg="blue", bg="white", font=(font, 16))
startButton.place(x=window_size/2-65,y=window_size/2-65)

# gui setting functions
def dot_numbers():
    global numbers
    if numbers == True:
        numbers = False
        numberButton.config(text="   dots   ")
    else:
        numbers = True
        numberButton.config(text="numbers")

def spaceSize_add():
    global space
    global spaceStr
    space += 1
    spaceStr = str(floor(space))
    spaceText.config(text="space: "+spaceStr)
    
def spaceSize_subtract():
    global space
    global spaceStr
    space -= 1
    spaceStr = str(floor(space))
    spaceText.config(text="space: "+spaceStr)

colorselector = 0
def colorMixer():
    global color
    global colorselector
    colorselector +=1
    if colorselector >= len(colorList):
        colorselector = 0
    color = colorList[colorselector]
    colorButton.config(fg=color)
    

# gui setting buttons
numberButton = Button(win, text="numbers", command=dot_numbers, font=(font, 16))
numberButton.place(x=10,y=window_size-55)

spaceSubtract = Button(win, text="-", command=spaceSize_subtract, font=(font, 16))
spaceStr = str(floor(space))
spaceText = Label(win, text="space: "+spaceStr , font=(font, 16), bg="white")
spaceAdd = Button(win, text="+", command=spaceSize_add, font=(font, 16))
spaceSubtract.place(x=140,y=window_size-55)
spaceText.place(x=180,y=window_size-50)
spaceAdd.place(x=290,y=window_size-55)

colorButton = Button(win, text="color", font=(font, 16), fg=color, command=colorMixer)
colorButton.place(x=350,y=window_size-55)

#update
win.after(speed, main)
win.mainloop()