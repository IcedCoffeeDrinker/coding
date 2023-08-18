import tkinter as tk
import numpy as np
from math import *
from time import sleep

# settings
window_height = 700
window_width = 700

# window
win = tk.Tk()
win.title("Rocket")
win.resizable(False, False)
win.geometry(f"{window_width}x{window_height}")
win.configure(background="#000000")
can = tk.Canvas(win, width=window_width, height=window_height, bg="#000000", highlightthickness=0)
can.place(x=0, y=0)

class Object:
    def __init__(self, shape_path, offset=[0, 0], scale=0):
        self.vertices, self.edges = self.load_obj(shape_path)
        self.rotation_speed = 1  # degrees
        self.vector_size = 5
        self.line_width = 1

        self.vector_size *= 0.5
        self.rotation_speed *= pi / 180
        self.offset = offset
        self.scale = scale

    def rotate(self, object, x, y, z):
        x_rotation = np.array([
            [1, 0, 0],
            [0, cos(x), -sin(x)],
            [0, sin(x), cos(x)]
        ])
        y_rotation = np.array([
            [cos(y), 0, sin(y)],
            [0, 1, 0],
            [-sin(y), 0, cos(y)]
        ])
        z_rotation = np.array([
            [cos(z), -sin(z), 0],
            [sin(z), cos(z), 0],
            [0, 0, 1]
        ])
        new_object = []
        for vector in object:
            new_vector = vector @ x_rotation @ y_rotation @ z_rotation
            new_object.append(new_vector)
        return new_object

    def project(self, object):
        orthographic_projection = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])
        return [vector @ orthographic_projection for vector in object]

    def draw(self, vertices):
        for vector in vertices:
            x, y = vector[:2]
            can.create_oval(x - self.vector_size, y - self.vector_size, x + self.vector_size, y + self.vector_size,
                            fill='white', width=0)
        for edge in self.edges:
            vertex = vertices[edge[0]]
            vertex1 = vertices[edge[1]]
            can.create_line(vertex[0], vertex[1], vertex1[0], vertex1[1], width=self.line_width, fill='white')

    def translate(self, object, size, offset):
        return [[vector[0] * size + offset[0] + window_width // 2,
                 -vector[1] * size - offset[1] + window_height // 2]
                for vector in object]

    def load_obj(self, file_path):
        vertices = []
        faces = []
        edges = []
        with open(file_path, 'r') as file:
            for line in file:
                tokens = line.split()
                if not tokens:
                    continue
                if tokens[0] == 'v':
                    vertex = tuple(float(x) for x in tokens[1:])
                    vertices.append(vertex)
                elif tokens[0] == 'l':
                    edge = tuple(int(i) - 1 for i in tokens[1:])
                    edges.append(edge)
                elif tokens[0] == 'f':
                    face = []
                    for token in tokens[1:]:
                        index = int(token.split('//')[0]) - 1  # Extract the vertex index and adjust for 0-based indexing
                        face.append(index)
                    faces.append(face)
                    # Add edges from the face
                    for i in range(len(face)):
                        edge = tuple(sorted((face[i], face[(i + 1) % len(face)])))
                        edges.append(edge)
        return vertices, edges

obj_object = Object('objs/fox.obj', [-70, 50], 4)

while True:
    can.delete('all')
    obj_object.vertices = obj_object.rotate(obj_object.vertices, obj_object.rotation_speed, obj_object.rotation_speed, obj_object.rotation_speed)
    projection = obj_object.project(obj_object.vertices)
    projection = obj_object.translate(projection, obj_object.scale, obj_object.offset)
    obj_object.draw(projection)
    win.update()
    sleep(0.01)  # Adding a small sleep time can reduce CPU usage

win.mainloop()
