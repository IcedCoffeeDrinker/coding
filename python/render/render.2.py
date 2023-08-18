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
    def __init__(self, shape_path, offset=[0,0], scale=0):
        self.vertices, self.edges = self.load_obj(shape_path)
        self.rotationSpeed = 1 # degrees
        self.vectorSize = 5
        self.lineWidth = 1

        self.vectorSize *= 0.5
        self.rotationSpeed *= pi / 180
        self.offset = offset
        self.scale = scale
        self.loop()

    def loop(self):
        while True:
            can.delete('all')
            self.vertices = self.rotate(self.vertices, self.rotationSpeed, self.rotationSpeed, self.rotationSpeed)
            projection = self.project(self.vertices)
            projection = self.translate(projection, self.scale, self.offset)
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

    def draw(self, vertices):
        for vector in vertices:
            x = vector[0]
            y = vector[1]
            can.create_oval(x-self.vectorSize, y-self.vectorSize, x+self.vectorSize, y+self.vectorSize, fill='white', width=0)
        for edge in self.edges:
            vertex = vertices[edge[0]]
            vertex1 = vertices[edge[1]]
            can.create_line(vertex[0], vertex[1], vertex1[0], vertex1[1], width=self.lineWidth, fill='white')

    def translate(self, object, size, offset):
        newObject = []
        for vector in object:
            vector[0] += offset[0]
            vector[1] -= offset[1]
            x = vector[0] * size
            y = vector[1] * -1 * size
            x += window_width / 2
            y += window_height / 2
            newObject.append([x, y])
        return newObject

    def load_obj(self, file_path): # by gpt
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


obj_object = object('objs/fox.obj', [-70, 50], 4)
#obj_object = object('objs/cube.obj', [0, 0], 100)
win.mainloop()
