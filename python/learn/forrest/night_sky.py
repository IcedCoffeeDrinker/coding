from turtle import *
from random import randint

def star(x,y,size):
    width(size*0.1)
    for i in range(6):
        color("yellow")
        up()
        goto(x,y)
        down()
        fd(size)
        lt(360/6)


def night_sky_main(amount):
    bgcolor("#272640")

    for i in range(amount):
        star(randint(-400,400),randint(-80,300),randint(1,20))

#night_sky_main(300)
