import pygame

class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Wireframe:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, coordinates):
        self.vertices.append(Vertex(*coordinates))

    def add_edge(self, start, end):
        self.edges.append(Edge(start, end))

    def project(self, vertex, camera):
        x, y, z = vertex.x - camera.x, vertex.y - camera.y, vertex.z - camera.z
        scale = 200 / (z + 200)
        x, y = x * scale + 400, y * scale + 300
        return int(x.item()), int(y.item())

    def draw(self, screen, camera):
        for edge in self.edges:
            start, end = self.vertices[edge.start], self.vertices[edge.end]
            x1, y1 = self.project(start, camera)
            x2, y2 = self.project(end, camera)
            pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2))
