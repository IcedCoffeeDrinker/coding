"""
Write a python program that shows a 3D cube rotating on two axis.
Every of the cubes faces shuld have a different brightness and the cube should be
rendered using ASCII characters. Use Tkinter.
Make sure the program can be run from a windows terminal.
"""

import tkinter as tk
import math

# Create the window
root = tk.Tk()
root.title("3D Cube")

# Create the canvas
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# Create the cube
cube_size = 200
cube_center = (200, 200)

# Create the cube faces
face_1 = canvas.create_polygon(cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                               cube_center[0] + cube_size/2, cube_center[1] - cube_size/2,
                               cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                               cube_center[0] - cube_size/2, cube_center[1] + cube_size/2,
                               fill="white", outline="white")

face_2 = canvas.create_polygon(cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                               cube_center[0] + cube_size/2, cube_center[1] - cube_size/2,
                               cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                               cube_center[0] - cube_size/2, cube_center[1] + cube_size/2,
                               fill="gray", outline="gray")

face_3 = canvas.create_polygon(cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                               cube_center[0] + cube_size/2, cube_center[1] - cube_size/2,
                               cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                               cube_center[0] - cube_size/2, cube_center[1] + cube_size/2,
                               fill="black", outline="black")

# Create the cube edges
edge_1 = canvas.create_line(cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                            cube_center[0] + cube_size/2, cube_center[1] - cube_size/2,
                            fill="white")

edge_2 = canvas.create_line(cube_center[0] + cube_size/2, cube_center[1] - cube_size/2,
                            cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                            fill="gray")

edge_3 = canvas.create_line(cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                            cube_center[0] - cube_size/2, cube_center[1] + cube_size/2,
                            fill="black")

edge_4 = canvas.create_line(cube_center[0] - cube_size/2, cube_center[1] + cube_size/2,
                            cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                            fill="white")

# Create the rotation variables
angle_x = 0
angle_y = 0

# Create the rotation function
def rotate_cube():
    global angle_x
    global angle_y

    # Rotate the cube around the x-axis
    angle_x += 0.1
    x = cube_center[0] + cube_size/2 * math.cos(angle_x)
    y = cube_center[1] + cube_size/2 * math.sin(angle_x)
    canvas.coords(face_1, cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                  x, y,
                  cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                  cube_center[0] - cube_size/2, cube_center[1] + cube_size/2)

    # Rotate the cube around the y-axis
    angle_y += 0.1
    x = cube_center[0] + cube_size/2 * math.cos(angle_y)
    y = cube_center[1] + cube_size/2 * math.sin(angle_y)
    canvas.coords(face_2, cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                  x, y,
                  cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                  cube_center[0] - cube_size/2, cube_center[1] + cube_size/2)

    # Rotate the cube around the z-axis
    canvas.coords(face_3, cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                  cube_center[0] + cube_size/2, cube_center[1] - cube_size/2,
                  cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                  cube_center[0] - cube_size/2, cube_center[1] + cube_size/2)

    # Rotate the edges
    canvas.coords(edge_1, cube_center[0] - cube_size/2, cube_center[1] - cube_size/2,
                  x, y)
    canvas.coords(edge_2, x, y,
                  cube_center[0] + cube_size/2, cube_center[1] + cube_size/2)
    canvas.coords(edge_3, cube_center[0] + cube_size/2, cube_center[1] + cube_size/2,
                  cube_center[0] - cube_size/2, cube_center[1] + cube_size/2)
    canvas.coords(edge_4, cube_center[0] - cube_size/2, cube_center[1] + cube_size/2,
                  cube_center[0] - cube_size/2, cube_center[1] - cube_size/2)

    # Call the function again
    root.after(10, rotate_cube)

# Call the function
rotate_cube()

# Run the program
root.mainloop()
