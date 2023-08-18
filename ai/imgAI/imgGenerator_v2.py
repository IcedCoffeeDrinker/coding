import tkinter as tk
import customtkinter as ck
from math import floor, sqrt

# setup custom appearance
ck.set_appearance_mode("dark")
ck.set_default_color_theme("green")

# create main window and set properties
win = ck.CTk()
win.geometry("800x500")
win.resizable(False, False)

# create main canvas and sidebar frames
frame = ck.CTkFrame(master=win, height=470, width=470)
frame.place(x=15, y=15)
sidebar = ck.CTkFrame(master=win, height=470, width=285)
sidebar.place(x=500, y=15)
slider1 = ck.CTkSlider(master=sidebar, orientation="horisontal")
#slider1.pack()
#slider1.place(x=500, y=50)


# bind mouse events
mouse = None
def motion(event):
    global mouse
    mouse = event.x, event.y
win.bind('<Motion>', motion)

click = False
def leftclick(state):
    global click
    click = not click
win.bind("<Button-1>", leftclick)

# Canvas class
class Canvas:
    def __init__(self):
        self.Xoffset = 15
        self.Yoffset = 15
        self.size = 470 - self.Xoffset * 2
        self.tile_amount = 28
        self.tile_size = self.size / self.tile_amount
        self.thickness_factor = 0.2
        self.steepniss_factor = 5
        self.displayed_tiles = []
        self.old_x = None
        self.old_y = None

        # create canvas
        self.canvas = tk.Canvas(frame, width=self.size, height=self.size, bg="black", highlightthickness=0)
        self.canvas.place(x=self.Xoffset, y=self.Yoffset)

        # create labels for mouse and grid positions
        self.mouse_label = ck.CTkLabel(master=sidebar, text="", font=ck.CTkFont(size=20, weight="bold"))
        self.mouse_label.place(x=15, y=15)
        self.grid_label = ck.CTkLabel(master=sidebar, text="", font=ck.CTkFont(size=20, weight="bold"))
        self.grid_label.place(x=15, y=45)

        self.grid_pos = None
        self.generate_tiles()

    # generate tiles
    def generate_tiles(self):
        self.tiles = [[0 for _ in range(self.tile_amount)] for _ in range(self.tile_amount)]
        self.displayed_tiles = [[None for _ in range(self.tile_amount)] for _ in range(self.tile_amount)]

    # draw a tile on the canvas
    def draw_tile(self, column, row):
        x = column * self.tile_size
        y = row * self.tile_size

        if x != self.old_x or y != self.old_y:
             self.old_x, self.old_y = x, y
             for loc_row in range(len(self.tiles)):
                for loc_column in range(len(self.tiles[0])):
                    row_distance = abs(row - loc_row)
                    column_distance = abs(column - loc_column)
                    distance = sqrt(row_distance **2 + column_distance **2)
                    if distance == 0:
                        tile_strenght = 1
                    else:
                        tile_strenght = round(self.thickness_factor / (distance **2 * self.steepniss_factor), 2)
                    self.tiles[loc_row][loc_column] += tile_strenght
                    if self.tiles[loc_row][loc_column] > 1:
                        self.tiles[loc_row][loc_column] = 1
                    tile_strenght = self.tiles[loc_row][loc_column]

                    value = int(floor(tile_strenght * 255))
                    color = '#%02x%02x%02x' % (value, value, value)
                    self.canvas.delete(self.displayed_tiles[loc_row][loc_column])
                    loc_x = loc_column * self.tile_size
                    loc_y = loc_row * self.tile_size
                    tile = self.canvas.create_rectangle(loc_x, loc_y, loc_x + self.tile_size, loc_y + self.tile_size, fill=color, width=0)
                    self.displayed_tiles[loc_row][loc_column] = tile



    # update labels
    def update_text(self):
        self.mouse_label.configure(text=mouse)
        self.grid_label.configure(text=self.grid_pos)

    # track mouse position
    def mouse_pos(self):
        global mouse, click
        if mouse is not None:
            grid_x = floor(mouse[0] / self.tile_size)
            grid_y = floor(mouse[1] / self.tile_size)
            self.grid_pos = grid_x, grid_y
            if (
                grid_x < self.tile_amount and
                grid_y < self.tile_amount and
                self.tiles[grid_y][grid_x] != 1 and
                click
            ):
                self.draw_tile(grid_x, grid_y)
        self.update_text()
        win.after(1, self.mouse_pos)

area = Canvas()
win.after(1,area.mouse_pos)
win.mainloop()
