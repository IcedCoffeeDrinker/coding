from tkinter import *
from math import *

#settings
window_size = 500
space = window_size / 20

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

def activate():
    global run
    run = True
    startButton.destroy()

# main
def main():
    global run
    global steps
    global digit
    global neededSteps
    global direction
    global xpo
    global ypo
    
    if run == True:
        # 1. print
        label = Label(win, text=digit, bg="white")
        label.place(x=xpo,y=ypo)
        print("digit: ", digit, " neededSteps: ", neededSteps, " direction: ", direction)
        
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
        
        
    win.after(100, main)




# start
startButton = Button(win, text="start", padx=50, pady=50, command=activate, fg="blue", bg="white")
startButton.place(x=window_size/2-65,y=window_size/2-65)

#update
win.after(100, main)
win.mainloop()