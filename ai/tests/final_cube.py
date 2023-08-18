import tkinter as tk
import math

class Cube:
    def __init__(self, root, size=100):
        self.root = root
        self.size = size
        self.angle_x = 0
        self.angle_y = 0
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

    def rotate_x(self, angle):
        self.angle_x = angle
        self.render()

    def rotate_y(self, angle):
        self.angle_y = angle
        self.render()

    def render(self):
        self.canvas.delete("all")
        vertices = [
            (1, 1, 1),
            (1, -1, 1),
            (-1, -1, 1),
            (-1, 1, 1),
            (1, 1, -1),
            (1, -1, -1),
            (-1, -1, -1),
            (-1, 1, -1)
        ]
        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7)
        ]
        size = self.size / 2
        center = 200
        for i in range(8):
            x, y, z = vertices[i]
            x, y = self.rotate_z(x, y, self.angle_x)
            x, z = self.rotate_y(x, z, self.angle_y)
            x = center + x * size
            y = center + y * size
            vertices[i] = x, y

        for edge in edges:
            x1, y1 = vertices[edge[0]]
            x2, y2 = vertices[edge[1]]
            self.canvas.create_line(x1, y1, x2, y2)

    @staticmethod
    def rotate_z(x, y, angle):
        radians = math.radians(angle)
        c, s = math.cos(radians), math.sin(radians)
        return c * x - s * y, s * x + c * y

    @staticmethod
    def rotate_y(x, z, angle):
        radians = math.radians(angle)
        c, s = math.cos(radians), math.sin(radians)
        return c * x + s * z, -s * x + c * z

root = tk.Tk()
root.title("Rotating Cube")
cube = Cube(root)

def change_x(value):
    cube.rotate_z(int(value))

def change_y(value):
    cube.rotate_y(int(value))

tk.Scale(root, from_=-360, to=360, orient=tk.HORIZONTAL, command=change_x).pack()
tk.Scale(root, from_=-360, to=360, orient=tk.HORIZONTAL, command=change_y).pack()
root.mainloop()
