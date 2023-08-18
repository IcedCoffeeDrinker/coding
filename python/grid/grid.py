from tkinter import *
from pynput.mouse import Controller
import winsound

# settings
window_size = 1000 # meaning here: canvas size
speed = 10
tileNumber = 10

# window
win = Tk()
win.title("grid selector")
win.attributes("-fullscreen", True)
win.configure(background="gray")

# variables
tileSize = window_size / tileNumber
coordinates = []
for row in range(tileNumber):
    for tile in range(tileNumber):
        x = tile * tileSize
        y = row * tileSize
        x1 = x + tileSize
        y1 = y + tileSize
        local_coordinates = [x, y, x1, y1]
        coordinates.append(local_coordinates)
# print(coordinates)
oldcords = 0

# mouse position
my_mouse = Controller()

# cancas
canvas = Canvas(win, width=window_size, height=window_size, bg="white")
canvas.place(x=0,y=0)

#main
def main():
    global oldcords
    mouse_x = my_mouse.position[0]
    mouse_y = my_mouse.position[1]
    for i in range(len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        x1 = coordinates[i][2]
        y1 = coordinates[i][3]
        if x < mouse_x and x1 > mouse_x and y < mouse_y and y1 > mouse_y:
            canvas.delete("all")
            canvas.create_rectangle(x, y, x1, y1, fill="aqua", width=0)
            if coordinates[i] != oldcords:
                oldcords = coordinates[i]
                winsound.PlaySound("click.wav", winsound.SND_ASYNC)
        else:
            canvas.create_rectangle(x, y, x1, y1, fill="white", width=0)
    win.after(speed, main)


win.after(speed, main)
win.mainloop()