import tkinter as tk
import customtkinter as ck
from math import *


# setup
ck.set_appearance_mode("dark")
ck.set_default_color_theme("green")
win = ck.CTk()
win.geometry("800x500")
win.resizable(False, False)

frame = ck.CTkFrame(master=win, height=470, width=470)
frame.place(x=15, y=15)

sidebar = ck.CTkFrame(master=win, height=470, width=285)
sidebar.place(x=500, y=15)
slider1 = ck.CTkSlider(sidebar, orientation="horizontal")
slider1.place

# rest
mouse = None
def motion(event):
    global mouse
    mouse = event.x, event.y
win.bind('<Motion>', motion)

click = False
def leftclick(state):
    global click
    if click == True:
        click = False
    else:
        click = True
win.bind("<Button-1>", leftclick)


class Canvas:
    def __init__(self):
        self.Xoffset = 15
        self.Yoffset = 15
        self.size = 470 - self.Xoffset * 2
        self.tileAmount = 28
        self.tileSize = self.size / self.tileAmount
        self.canvas = tk.Canvas(frame, width=self.size, height=self.size, bg="white")
        self.canvas.place(x=self.Xoffset,y=self.Yoffset)
        self.grid_pos = None

        self.mouse_label = ck.CTkLabel(master=sidebar, text="", font=ck.CTkFont(size=20, weight="bold"))
        self.mouse_label.place(x=15,y=15)
        self.grid_label= ck.CTkLabel(master=sidebar, text="", font=ck.CTkFont(size=20, weight="bold"))
        self.grid_label.place(x=15,y=45)

        self.generate_tiles()

    def generate_tiles(self):
        self.tiles = []
        for row in range(self.tileAmount):
            tiles = []
            for column in range(self.tileAmount):
                tiles.append(0)
            self.tiles.append(tiles)
            print(tiles)

    def draw_tile(self, column, row): # x,y
        x = column * self.tileSize
        y = row * self.tileSize
        tile = self.canvas.create_rectangle(x, y, x + self.tileSize, y + self.tileSize, fill="black", width=0)

    def update_text(self):
        self.mouse_label.configure(text=mouse)
        self.grid_label.configure(text=self.grid_pos)

    def mouse_pos(self):
        global click
        if mouse != None:
            self.grid_pos = [floor(mouse[0] / self.tileSize), floor(mouse[1] / self.tileSize)]
            if self.grid_pos[0] < self.tileAmount and self.grid_pos[1] < self.tileAmount:
                if self.tiles[self.grid_pos[1]][self.grid_pos[0]] != 1 and click == True:
                    self.draw_tile(self.grid_pos[0], self.grid_pos[1])
                    self.tiles[self.grid_pos[1]][self.grid_pos[0]] = 1
                    for i in self.tiles:
                        print(i)

        self.update_text()
        win.after(1,self.mouse_pos)


area = Canvas()
win.after(1,area.mouse_pos)
win.mainloop()
