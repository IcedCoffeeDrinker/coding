from turtle import *
from random import *
import night_sky
import christmas_tree

def draw_floor():
    up()
    goto(-400,-300)
    down()
    color("#524632")
    begin_fill()
    goto(400,-300)
    goto(400,-90)
    goto(-400,-90)
    goto(-400,-300)
    end_fill()

def main():
    screen = Screen()
    screen.setup(800,600) # feste Fenstergröße
    tracer(10)

    draw_floor()
    night_sky.night_sky_main(120)
    christmas_tree.tree_main(25)

main()
exitonclick() # verhindert vorzeitiges schließen von turtle (schließt bei Klick)
