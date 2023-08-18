from vpython import *
import time
print("modules loaded")

# selected part
selection = ["sphere", "cube", "box", "tube", "position", "room", "move", "size2.0", "transpatent", "delete"]
select = selection[9]

if select == "sphere":
    #create ball
    ball = sphere(color=color.red)

    while True:
        time.sleep(1)
        ball.color=color.blue # change color
        print("change")
        time.sleep(1)
        ball.color=color.red # change color
        print("change")

if select == "cube":
    cube = box(color=color.yellow)

if select == "box":
    # len. = x, hei. = y, wid = z
    # more practical: size=vector(x,y,z) mantioned in size2.0
    box = box(color=color.magenta,length=10,width=5,height=5)

if select == "tube":
    # summons normaly sideways and is not centered
    # len. wid. and hei. also work
    tube = cylinder(color=color.magenta,length=30,radius=5)

if select == "position":
    # atention!!! if I used box = box(), box2 = box() -- it would refference the first box not the module
    box1 = box(pos=vector(-5,-5,-5),length=5,height=5,width=5,color=color.blue)
    box2 = box(pos=vector(5,5,5),length=5,height=5,width=5,color=color.red)
    print("lul")

if select == "room" or select == "move":
    marble = sphere(pos=vector(0,0,0),radius=1, color=color.magenta)
    floor = box(pos=vector(0,-5,0), length=10.1,height=0.1,width=10.1,color=color.white)
    roof = box(pos=vector(0,5,0), length=10.1,height=0.1,width=10.1,color=color.white)
    backwall = box(pos=vector(0,0,-5), length=10.1,height=10.1,width=0.1,color=color.white)
    leftwall = box(pos=vector(-5,0,0), length=0.1,height=10.1,width=10.1,color=color.white)
    righttwall = box(pos=vector(5,0,0), length=0.1,height=10.1,width=10.1,color=color.white)
    if select == "move":
        ypo = 0
        step = 0.1
        direction = "up"
        while True:
            marble.pos=vector(0,ypo,0) # change position
            if ypo >= 4:
                direction = "down"
            elif ypo <= -4:
                direction = "up"

            if direction =="up":
                ypo += step
            else:
                ypo -= step
            time.sleep(0.01)

if select == "size2.0":
    # all coordinates relative to object center!
    cube1 = box(pos=vector(0,1,0), size=vector(1,1,1))
    cube2 = box(pos=vector(0,-1,0), size=vector(1,1,1))

# use variables to determin the vectors!!!
# use variables to determin the vectors!!!
# use variables to determin the vectors!!!

if select == "transpatent":
     cube = box(pos=vector(0,0,0), size=vector(1,1,1), color=color.white, opacity=0.3)
     cube2 = box(pos=vector(0,0,0), size=vector(.1,.1,.1), color=color.red, opacity=0.3)

if select == "delete":
    cube = box(pos=vector(0,0,0), size=vector(1,1,1), color=color.white, opacity=0.3)

    time.sleep(3)

    cube.visible = False # delte cube visualy
    del cube # delete cube from memory

# important! prevents error for running window with programm ended
while True:
    pass
