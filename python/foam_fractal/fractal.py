from vpython import *
import time
from pynput.keyboard import *
print("modules loaded")

# create box
class cube:
    def __init__(self, xpo, ypo, zpo, size):
        self.xpo = xpo
        self.ypo = ypo
        self.zpo = zpo
        self.size = size
        newCube = box(pos=vector(xpo,ypo,zpo), size=vector(size,size,size), color=vector(0.207, 0.360, 0.490))
        elements.append(newCube)

# variables
size = 99
cords = [[0,0,0,size]]
newCords = []
elements = []
eturation = 0
# #355c7d
# 0.207, 0.360, 0.490

# #f67280
# 0.964, 0.447, 0.501

def show():
    for selected in cords:
        newCube = cube(selected[0],selected[1],selected[2],selected[3])

def delete():
    global elements
    for element in elements:
        element.visible = False
        del element
    elements = []

def transform():
    global size
    global newCords
    global cords
    for selected in range(len(cords)):
        x = cords[selected][0]
        y = cords[selected][1]
        z = cords[selected][2]
        size = cords[selected][3]

        newsize = size/3
        size = newsize # bruh
        # box1.1
        newx = x - newsize
        newy = y - newsize
        newz = z - newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box1.2
        newx = x
        newy = y - newsize
        newz = z - newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box1.3
        newx = x + newsize
        newy = y - newsize
        newz = z - newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box1.4
        newx = x - newsize
        newy = y
        newz = z - newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box1.5
        # empty

        # box1.6
        newx = x + newsize
        newy = y
        newz = z - newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box1.7
        newx = x - newsize
        newy = y + newsize
        newz = z - newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box1.8
        newx = x
        newy = y + newsize
        newz = z - newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box1.9
        newx = x + newsize
        newy = y + newsize
        newz = z - newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)
#-------------------------------------------------
        # box2.1
        newx = x - newsize
        newy = y - newsize
        newz = z
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box2.2
        # empty

        # box2.3
        newx = x + newsize
        newy = y - newsize
        newz = z
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box2.4
        # empty

        # box2.5
        # empty

        # box2.6
        # empty

        # box2.7
        newx = x - newsize
        newy = y + newsize
        newz = z
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box2.8
        # empty

        # box2.9
        newx = x + newsize
        newy = y + newsize
        newz = z
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)
#-------------------------------------------------
        # box3.1
        newx = x - newsize
        newy = y - newsize
        newz = z + newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box3.2
        newx = x
        newy = y - newsize
        newz = z + newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box3.3
        newx = x + newsize
        newy = y - newsize
        newz = z + newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box3.4
        newx = x - newsize
        newy = y
        newz = z + newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box3.5
        # empty

        # box3.6
        newx = x + newsize
        newy = y
        newz = z + newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box3.7
        newx = x - newsize
        newy = y + newsize
        newz = z + newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box3.8
        newx = x
        newy = y + newsize
        newz = z + newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

        # box3.9
        newx = x + newsize
        newy = y + newsize
        newz = z + newsize
        newCube = [newx,newy,newz,newsize]
        newCords.append(newCube)

    cords = newCords
    newCords = []

def eturationSelection():
    try:
        maxeturations = "lul"
        maxeturations = int(input("Enter number of eturations to be calculated: "))
    except ValueError:
        print("Enter a number")
        eturationSelection()
    return maxeturations

def eturate():
    if maxeturations > eturation:
        transform()
#        print(elements)
        delete()
        show()
#----------------------------------------
def press_on(key):
    if key == Key.esc:
        return False
    if key == Key.space:
        eturate()
        time.sleep(2)

def press_off(key):
    pass

#----------------------------------------

def main():
    # window
    scene = canvas(width=1280, height=800,
    center=vector(0,0,0), background=vector(0.964, 0.447, 0.501))
    scene.ambient=color.gray(1)

    global maxeturations
    maxeturations = eturationSelection()
    print(type(maxeturations))
    # fractal
    fractal = cube(cords[0][0],cords[0][1],cords[0][2],cords[0][3])
    elements.append(fractal)
    while True:
        with Listener(on_press = press_on, on_release = press_off)as listener:
            listener.join()

main()
