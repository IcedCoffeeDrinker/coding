from math import *
from color import *
from tqdm import tqdm
from PIL import Image

print("import finished")

# variables
resolution = float(input("Enter resolution: ")) # 1 = 100%  2 = 200%
max_eturations = int(input("Enter accuracy: ")) # 200 normal (accuracy)
renderPos_x = float(input("Enter x position: ")) # 0 is center
renderPos_y = float(input("Enter y position: "))
renderPos_y *= -1 # invert y
zoom = float(input("Enter zoom: ")) # 1 = normal 2 = double size
img_height = int(2160 * resolution)
img_width = int(3840 * resolution)
plane_width = 4/9*16

# imgage
img = Image.new(mode="RGB",size=(img_width,img_height))

# functions
def calculate(Cr,Ci): # input is C (real + imaginary)
    Z = [0,0]
    for eturation in range(max_eturations):
        r = Z[0]
        i = Z[1]
        localA = r**2 + i**2 *-1 +Cr # square complex numbers :)
        localB = r*i *2 +Ci
        Z = [localA,localB]
        if sqrt(localA*localA+localB*localB) > 2:
            return color(eturation,max_eturations,"255")
    if sqrt(localA*localA+localB*localB) <= 2:
        return True

def draw(x,y,color):
    try:
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
        img.putpixel((x,y), (r,g,b))
    except:
        print(color)

def process():
    for y in tqdm(range(img_height)):
        for x in range(img_width):
            a = plane_width/zoom/img_width*x-plane_width/2/zoom
            b = 4/zoom/img_height*y-2/zoom # convert x,y to complex plane
            a += renderPos_x
            b += renderPos_y
            inside = calculate(a,b)
            localX = x # screen cords
            localY = y
            if inside == True:
                draw(localX,localY,[0,0,0])
            else:
                color = inside
                draw(localX,localY,color)

# main
def main():
    print()
    process()
    print("all calculations done")
main()
img.show()
print("finished")
