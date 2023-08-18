"""
Write a program in python that  shows a white cube in a tkinter window.
Each of the cubes faces shuld have a different shade and the cube should be spinning on two axis in a loop.
The cube is rendered in 3d.
"""

from tkinter import *
from math import *
import time

root = Tk()
canvas = Canvas(root, width=500, height=500, bg='black')
canvas.pack()

class Cube:
    def __init__(self, canvas, x, y, size, colors):
        self.x = x
        self.y = y
        self.size = size
        self.colors = colors
        self.canvas = canvas
        self.angleX, self.angleY = 0, 0
        self.update()

    def project(self, x, y, z):
        return self.x + (x * self.size) / (z + self.size), self.y + (y * self.size) / (z + self.size)

    def update(self):
        points = [[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]]
        t = [[0, 1, 2, 3], [0, 4, 5, 1], [1, 5, 6, 2], [2, 6, 7, 3], [3, 7, 4, 0], [4, 7, 6, 5]]
        self.polygons = []
        for point in points:
            x, y = self.project(point[0], point[1], point[2])
            points[points.index(point)] = [x, y]
        for triangle in t:
            p1 = points[triangle[0]]
            p2 = points[triangle[1]]
            p3 = points[triangle[2]]
            p4 = points[triangle[3]]
            self.polygons.append([p1, p2, p3, p4])

    def rotateX(self, angle):
        self.angleX += angle
        for point in [[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]]:
            y = point[1]
            z = point[2]
            point[1] = y * cos(angle) - z * sin(angle)
            point[2] = z * cos(angle) + y * sin(angle)
        self.update()

    def rotateY(self, angle):
        self.angleY += angle
        for point in [[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]]:
            x = point[0]
            z = point[2]
            point[0] = x * cos(angle) - z * sin(angle)
            point[2] = z * cos(angle) + x * sin(angle)
        self.update()

    def draw(self):
        for polygon in self.polygons:
            self.canvas: Canvas
            self.canvas.create_polygon(polygon, fill=self.colors[self.polygons.index(polygon)], outline='black')

colors = ["red", "green", "blue", "white", "yellow", "purple"]
cube = Cube(canvas, 250, 250, 200, colors)

def update_cube():
    cube.rotateY(0.01)
    cube.rotateX(0.01)
    canvas.delete("all")
    cube.draw()
    root.after(10, update_cube)

root.after(0, update_cube)

root.mainloop()
