from tkinter import *
from math import *
import objects
# settings
window_height = 700
window_width = 700



# window
win = Tk()
win.title("Rocket")
win.resizable(False, False)
win.geometry(str(window_width) + "x" + str(window_height))
win.configure(background="#000000")
can = Canvas(win,width=window_width,height=window_height,bg="#000000",highlightthickness=0)
can.place(x=0,y=0)

class object:
    def __init__(self, shape):
        self.shape = shape
        self.rotationSpeed = 0.01 # degrees
        self.vectorSize = 10

        self.vectorSize *= 0.5
        self.rotationSpeed *= pi / 180
        self.loop()

    def loop(self):
        while True:
            can.delete('all')
            self.shape = self.rotate(self.shape, self.rotationSpeed, self.rotationSpeed, self.rotationSpeed)
            projection = self.project(self.shape)
            projection = self.translate(100, projection)
            self.draw(projection)
            win.update()

    def rotate(self, object, x, y, z):
        xRotation = [
        [1, 0, 0],
        [0, cos(x), -sin(x)],
        [0, sin(x), cos(x)]
        ]
        yRotation = [
        [cos(y), 0, sin(y)],
        [0, 1, 0],
        [-sin(y), 0, cos(y)]
        ]
        zRotation = [
        [cos(z), -sin(z), 0],
        [sin(z), cos(z), 0],
        [0, 0, 1]
        ]
        newObject = []
        for vector in object:
            newVector = self.matrixMultiplier(xRotation, vector)
            newVector = self.matrixMultiplier(yRotation, newVector)
            newVector = self.matrixMultiplier(zRotation, newVector)
            newObject.append(newVector)
        return newObject

    def matrixMultiplier(self, matrix, vector):     # matrix must have as many rows as vector has columns
        finalVector = [0, 0, 0]                        # assuming vector has only one row
        for row in range(len(matrix)):
            sum = 0
            for column in range(len(matrix[row])):
                sum += matrix[row][column] * vector[column]
            finalVector[row] += sum
        return finalVector

    def project(self, object):
        self.ortographicProjection = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
        newObject = []
        for vector in object:
            newVector = self.matrixMultiplier(self.ortographicProjection, vector)
            newObject.append(newVector)
        return newObject

    def draw(self, object):
        for vector in object:
            x = vector[0]
            y = vector[1]
            can.create_oval(x-self.vectorSize, y-self.vectorSize, x+self.vectorSize, y+self.vectorSize, fill='white')

    def translate(self, size, object):
        newObject = []
        for vector in object:
            x = vector[0] * size
            y = vector[1] * -1 * size
            x += window_width / 2
            y += window_height / 2
            newObject.append([x, y])
        return newObject

cube = object(objects.cube)
win.mainloop()
