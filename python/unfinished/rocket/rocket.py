from tkinter import *


# settings
window_height = 500
window_width = 500

#window
win = Tk()
win.title("Rocket")
win.resizable(False, False)
win.geometry(str(window_width) + "x" + str(window_height))
win.configure(background="#000000")

# functions
class rocket:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velocity = [0,0]
        self.orientation = 0

    def move(self):
        pass

def loop():
    pass

def main():
    pass

win.mainloop()
