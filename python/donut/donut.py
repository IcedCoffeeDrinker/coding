import math as m
import numpy as np
from asciimatics.screen import Screen
from matplotlib import pyplot as plt


class donut:
    def __init__(self):
        self.torusCircleResolution = 10
        self.torusResolution = 30
        self.torusCircleRadius = 0.3
        self.torusRadius = 1.5
        self.rotationSpeed = [0, 0, 0] # x, y, z
        self.zOffset = 3

        # camera settings
        self.fov = 10 # in degrees
        self.zOffset = 10

        self.S = 1 / m.tan(self.fov / 2 * m.pi / 180)
        self.n = 1 # far and near plane
        self.f = 10

        self.perspectiveMatrix = [
			[self.S, 0, 0, 0],
			[0, self.S, 0, 0],
			[0, 0, self.f / (self.f - self.n), 1],
			[0, 0, self.f * self.n / (self.f - self.n), 0]
		]
        self.torus = self.generateDonut()
        self.loop()

    def matrixMultiplier(self, matrix, vertex):
        final_vertex = []
        for row in range(len(matrix)):
            sum = 0
            for column in range(len(vertex)):
                sum += matrix[row][column] * vertex[column]
            final_vertex.append(sum)
            return final_vertex
    
    def rotate(self, vertex, axis, angle):
        if axis =='x':
            matrix = [[1, 0, 0],
                      [0, m.cos(angle), -m.sin(angle)],
                      [0, m.sin(angle), m.cos(angle)]]
        elif axis == 'y':
            matrix = [[m.cos(angle), 0, m.sin(angle)],
                      [0, 1, 0],
                      [-m.sin(angle), 0, m.cos(angle)]]
        elif axis == 'z':
            matrix = [[m.cos(angle), -m.sin(angle), 0],
                      [m.sin(angle), m.cos(angle), 0],
                      [0, 0, 1]]
        return self.matrixMultiplier(matrix, vertex)
            

    def generateDonut(self):
        circleStepSize = 2 * m.pi / self.torusCircleResolution
        circle = []
        for i in range(self.torusCircleResolution):
            vertex = [self.torusRadius+self.torusCircleRadius*m.cos(circleStepSize*i),
                      self.torusCircleRadius*m.cos(circleStepSize*i),
                      0]
            circle.append(vertex)
        torusStepSize = 2 * m.pi / self.torusResolution
        torus = []
        for i in range(self.torusResolution):
            newCircle = [self.rotate(circle[ii], 'y', torusStepSize*i) for ii in range(self.torusCircleResolution)]
            print(newCircle)
            torus += newCircle
        print('donut generated')
        return torus
    
    def rotateTorus(self):
        print(self.torus)
        for vertex in self.torus:
            vertex = self.rotate(vertex, 'x', self.rotationSpeed[0])
            vertex = self.rotate(vertex, 'y', self.rotationSpeed[1])
            vertex = self.rotate(vertex, 'z', self.rotationSpeed[2])

    def project(self):
        projection = []
        for vertex in self.torus:
            copyVertex = vertex.copy()
            copyVertex.append(1)
            copyVertex[2] += self.zOffset
            copyVertex = self.matrixMultiplier(self.perspectiveMatrix, copyVertex)
            copyVertex = [copyVertex[0] / copyVertex[3], copyVertex[1] / copyVertex[3], copyVertex[2] / copyVertex[3]]
            projection.append(copyVertex)
        return projection

    def ascii(self):
        pass
    
    def loop(self):
        self.rotateTorus()
        projection = self.project()
        #self.ascii(projection)

donut()