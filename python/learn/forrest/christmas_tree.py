from turtle import *
import random

def triangle(x,y,size,colorL):
    up()
    goto(x,y)
    color(colorL)
    down()
    begin_fill()
    fd(size/2)
    for i in range(2):
        lt(120)
        fd(size)
    lt(120)
    fd(size/2)
    end_fill()

def square(x,y,size,colorT):
    up()
    goto(x-size/2,y)
    color(colorT)
    down()
    begin_fill()
    for i in range(4):
        fd(size)
        lt(90)
    end_fill()

def tannenbaum(x,y,sizeT,colorL,colorT):
    square(x,y,sizeT,colorT)
    for i in range(3):
        y = y + sizeT*0.8
        triangle(x,y,sizeT*3-5*i,colorL)

def tree_main(amount):
    trees = []
    treesY = []
    for i in range(amount):
        x = random.randint(-400,400)
        y = random.randint(-300,-100)
        size = random.randint(20,60) # not used
        trees.append([x,y])
        treesY.append(y)
    treesY.sort(reverse=True)
    print(treesY)
    leaf_colors = ["#3F4E4F","#11340F","#354E32"]
    trunk_colors = ["#A27B5C","#533e2d"]
    for treeY in treesY:
        leaf_color = leaf_colors[random.randint(0,len(leaf_colors)-1)]
        trunk_color = trunk_colors[random.randint(0,len(trunk_colors)-1)]
        for tree in trees:
            if treeY == tree[1]:
                tannenbaum(tree[0],tree[1],50,leaf_color,trunk_color)

#tree_main(50)
