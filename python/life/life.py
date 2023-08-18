from tkinter import *
import time
from math import *
import round_canvas as round
import random

# settings - gui
window_width = 2000
window_height = floor(window_width / 16 * 10)
corner_radius= 20
sim_size = window_height * 0.8
sim_overlay_size = sim_size + corner_radius * 2
spacing = (window_height - sim_overlay_size) / 2
settings_posX = spacing*2+sim_overlay_size # overlay
settings_sizeX = window_width - sim_overlay_size - 3 * spacing # overlay
settings_sizeY = sim_overlay_size # overlay
settings_height = sim_size
settings_width = settings_sizeX - corner_radius * 2
color = ["#242A38","#4E586E","#FFFFFF","#F66763"]
slider_display_spacing = 400
font = "Helvetica"

# window
win = Tk()
win.title("Pi")
win.resizable(False, False)
win.geometry(str(window_width) + "x" + str(window_height))
win.configure(background=color[0])

# layout
canvas = Canvas(win, width=window_width, height=window_height, bg=color[0], highlightthickness=0)
canvas.place(x=0,y=0)

sim_overlay = round.round_rectangle(canvas, spacing, spacing, sim_overlay_size+spacing, sim_overlay_size+spacing, radius=corner_radius, fill=color[3])
sim_canvas = Canvas(win, width=sim_size, height=sim_size, bg=color[2], highlightthickness=0)
sim_canvas.place(x=spacing+corner_radius,y=spacing+corner_radius)

settings_overlay = round.round_rectangle(canvas, settings_posX, spacing, settings_posX+settings_sizeX, spacing+settings_sizeY, radius=corner_radius, fill=color[1])
settings_canvas = Canvas(win, width=settings_width, height=settings_height, bg=color[1], highlightthickness=0)
settings_canvas.place(x=settings_posX+corner_radius,y=spacing+corner_radius)

red_sliders = ["red amount","red red","red blue","red yellow","red green"]
blue_sliders = ["blue amount","blue red","blue blue","blue yellow","blue green"]
yellow_sliders = ["yellow amount","yellow red","yellow blue","yellow yellow","yellow green"]
green_sliders = ["green amount","green red","green blue","green yellow","green green"]
all_sliders = red_sliders+blue_sliders+yellow_sliders+green_sliders
slider_spacing = settings_height / len(all_sliders)
true_sliders = []
spacing_counter = 0
for slider in all_sliders:
    slider_name = Label(win,text=slider,font=(font, 16),fg=color[3],bg=color[1],anchor="w")
    slider_name.place(x=settings_posX+corner_radius+slider_display_spacing,y=spacing+corner_radius+slider_spacing*spacing_counter)
    slider = Scale(win,from_=-2,to=2,orient=HORIZONTAL,fg=color[2],bg=color[1],length=300,resolution=0.01)
    slider.place(x=settings_posX+corner_radius,y=spacing+corner_radius+slider_spacing*spacing_counter)
    true_sliders.append(slider)
    spacing_counter += 1

# simulation

# settings - sim
particle_size = 5
speed = 10

# variabes
particles = []


class particle:

    def __init__(self,position,velocity,color):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.old_pos = position

    def show(self):
        x = self.position[0]
        y = self.position[1]
        self.point = sim_canvas.create_oval(x-particle_size/2,y-particle_size/2,x+particle_size/2,y+particle_size/2,fill=self.color,width=0)

    def relation(self):
        g = 0.01 # temporary

        for particle2 in particles:
            p2X = particle2.position[0]
            p2Y = particle2.position[1]
            fx = 0
            fy = 0
            dx = self.position[0]-p2X
            dy = self.position[1]-p2Y
            distance = sqrt(dx*dx+dy*dy)
            if distance != 0:
                F = g * 1 / distance
                fx += F * dx
                fy += F * dy

            self.velocity[0] += fx
            self.velocity[1] += fy
            self.position[0] -= self.velocity[0]
            self.position[1] -= self.velocity[1]
            if self.position[0] <= 0 or self.position[0] >= sim_size:
                self.velocity[0] *= -1
            if self.position[1] <= 0 or self.position[1] >= sim_size:
                self.velocity[1] *= -1

    def redraw(self):
        sim_canvas.delete(self.point)
        self.show()


def create(amount,color):
    global particles
    for i in range(amount):
        local_particle = particle([random.random()*sim_size,random.random()*sim_size],[0,0],color)
        particles.append(local_particle)

def draw():
    for particle in particles:
        particle.show()

def calculate():
    for particle in particles:
        particle.relation()

def redraw():
    for particle in particles:
        particle.redraw()

# main
create(10,"red")
draw()

def loop():
    calculate()
    redraw()
    win.after(speed,loop)
loop()

win.mainloop()
