import tkinter as tk
import math

# Create the root window
root = tk.Tk()
root.title("3D Cube")
root.geometry("600x600")

# Set the background color of the root window to white
root.configure(bg="white")

# Set the dimensions of the canvas
canvas_width = 600
canvas_height = 600

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Define the vertices of the cube in 3D space
vertices = [
    [-1, -1, -1],  # 0
    [1, -1, -1],   # 1
    [1, 1, -1],    # 2
    [-1, 1, -1],   # 3
    [-1, -1, 1],   # 4
    [1, -1, 1],    # 5
    [1, 1, 1],     # 6
    [-1, 1, 1]     # 7
]

# Define the edges of the cube
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4]
]

# Define the faces of the cube
# Each face is defined as a list of vertices that form the face
faces = [
    [0, 1, 2, 3],  # front
    [0, 1, 5, 4],  # right
    [1, 2, 6, 5],  # top
    [2, 3, 7, 6],  # back
    [3, 0, 4, 7],  # left
    [4, 5, 6, 7]   # bottom
]

# Define the colors of the faces of the cube
# Each color is represented as a tuple of (R, G, B) values
face_colors = [
    (255, 0, 0),   # front
    (0, 255, 0),   # right
    (0, 0, 255),   # top
    (255, 255, 0), # back
    (0, 255, 255), # left
    (255, 0, 255)  # bottom
]

# Function to project a 3D point onto a 2D plane
# This function takes in a 3D point (x, y, z) and returns a 2D point (x, y)
def project(point):
    x, y, z = point
    return (x, y)

# Function to rotate a 3D point around the x-axis
# This function takes in a 3D point (x, y, z) and an angle in degrees
# It returns the rotated point
def rotate_x(point, angle):
    x, y, z = point
    radians = math.radians(angle)
    cosa = math.cos(radians
