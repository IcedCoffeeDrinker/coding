import time

# Define the size of the cube (in characters)
size = 5

# Define the different faces of the cube
face1 = [" "] * size
face2 = [" "] * size
face3 = [" "] * size
face4 = [" "] * size
face5 = [" "] * size
face6 = [" "] * size

for i in range(size):
    face1[i] = "*"
    face2[i] = "*"
    face3[i] = "*"
    face4[i] = "*"
    face5[i] = "*"
    face6[i] = "*"

# Define the initial orientation of the cube
cube = [face1, face2, face3, face4, face5, face6]

# Function to rotate the cube 90 degrees clockwise
def rotate_cube(cube):
    new_cube = [[] for i in range(size)]
    for i in range(size):
        for j in range(size):
            new_cube[i].append(cube[size-1-j][i])
    return new_cube

# Loop to continuously display the rotating cube
while True:
    # Rotate the cube by a small angle each time it is displayed
    for angle in range(0, 360, 10):
        # Print each face of the cube as a single block
        for face in cube:
            print("".join(face))
        print()
        time.sleep(0.5)
        cube = rotate_cube(cube)
