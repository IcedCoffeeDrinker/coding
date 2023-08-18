from math import *
from color import *
from tqdm import tqdm
from PIL import Image

print("import finished")

# variables
resolution = float(input("Enter resolution: ")) # 1 = 100%  2 = 200%
max_eturations = int(input("Enter accuracy: ")) # 200 normal (accuracy)
img_height = int(2160 * resolution)
img_width = int(3840 * resolution)
cords = []

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
        cords.append([])
        for x in range(img_height):
            a = 4/img_height*x-2 # convert x,y to complex plane
            b = 4/img_height*y-2
            inside = calculate(a,b)
            localX = x # screen cords
            localY = y
            if inside == True:
                draw(localX,localY,[0,0,0])
            else:
                color = inside
                draw(localX,localY,color)
                cords[y].append([localX,localY,inside])

# main
def main():
    print()
    process()
    print("all calculations done")
main()
img.show()
print("finished")
