import tkinter as tk
from math import sin, cos, pi
import objects

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
    def __init__(self, shape):
        self.shape = shape
        self.rotation_speed = 0.01 * pi / 180  # degrees to radians
        self.vector_size = 5
        
        self.loop()

    def loop(self):
        while True:
            can.delete('all')
            self.shape = self.rotate(self.shape, self.rotation_speed, self.rotation_speed, self.rotation_speed)
            projection = self.project(self.shape)
            projection = self.translate(100, projection)
            self.draw(projection)
            win.update()

    def rotate(self, object, x, y, z):
        x_rotation = [
            [1, 0, 0],
            [0, cos(x), -sin(x)],
            [0, sin(x), cos(x)]
        ]
        y_rotation = [
            [cos(y), 0, sin(y)],
            [0, 1, 0],
            [-sin(y), 0, cos(y)]
        ]
        z_rotation = [
            [cos(z), -sin(z), 0],
            [sin(z), cos(z), 0],
            [0, 0, 1]
        ]

        return [
            self.matrix_multiplier(
                z_rotation,
                self.matrix_multiplier(
                    y_rotation,
                    self.matrix_multiplier(x_rotation, vector)
                )
            )
            for vector in object
        ]

    @staticmethod
    def matrix_multiplier(matrix, vector):
        return [sum(matrix[row][col] * vector[col] for col in range(len(matrix[row]))) for row in range(len(matrix))]

    def project(self, object):
        ortographic_projection = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]

        return [self.matrix_multiplier(ortographic_projection, vector) for vector in object]

    def draw(self, object):
        for vector in object:
            x, y = vector
            can.create_oval(x - self.vector_size, y - self.vector_size, x + self.vector_size, y + self.vector_size, fill='white')



    @staticmethod
    def translate(size, object):
        center_x, center_y = window_width / 2, window_height / 2
        return [[vector[0] * size + center_x, -vector[1] * size + center_y] for vector in object]

cube = Object(objects.cube)
win.mainloop()
