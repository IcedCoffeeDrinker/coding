from tkinter import *
from math import *

# settings
scaleFactor = 2
win_width = 350 * scaleFactor
win_height = 300 * scaleFactor
can_width = 300 * scaleFactor
can_height = 300 * scaleFactor

# window setup
win = Tk()
win.geometry(str(win_width)+"x"+str(win_height))
win.resizable(False,False)
can = Canvas(win, width=can_width, height=can_height, bg="black")
can.place(x=0, y=0)
scale = Scale(win, from_=0, to=180, orient=VERTICAL, resolution=0.1, variable=45, width=10 * scaleFactor, length=280 * scaleFactor)
scale.place(x=325 * scaleFactor, rely=0.5, anchor=CENTER)

# suff
class tree:
    def __init__(self):
        self.depth = 10
        self.branchSize = 100 * scaleFactor
        self.branchFactor = 0.5
        self.angle = pi*2 / 8
        self.start = [can_width / 2, can_height]

        self.generate()

    def generate(self):
        x, y = self.start
        branchEnds = [[x, y - self.branchSize, 0]]
        can.create_line(x, y, branchEnds[0][0], branchEnds[0][1], fill="white", width=1)

        for eturation in range(self.depth):
            newBranchEnds = []
            for startPoint in branchEnds:
                branchLength = self.branchSize * (self.branchFactor / (eturation+1))
                angle = startPoint[2] + self.angle
                angle1 = startPoint[2] - self.angle
                trunk = self.rotate(branchLength, angle)
                trunk1 = self.rotate(branchLength, angle1)
                x = startPoint[0]
                y = startPoint[1]
                x1 = x - trunk[0]
                y1 = y - trunk[1]
                x2 = x - trunk1[0]
                y2 = y - trunk1[1]
                can.create_line(x, y, x1, y1, fill="white", width=1)
                can.create_line(x, y, x2, y2, fill="white", width=1)
                newBranchEnds.append([x1,y1,angle])
                newBranchEnds.append([x2,y2,angle1])
            branchEnds = newBranchEnds

    def delete(self):
        can.delete("all")

    def rotate(self, branchLength, angle):
        x = branchLength * cos(angle + pi/2) # unit circle starts at 0,1 and rotates counter clockwise
        y = branchLength * sin(angle + pi/2) # so add 90 degrees
        return x,y

    def draw(self,x,y,x1,y1):
        can.create_line(x, y, x1, y1, fill="white")

def update(angle):
    global Tree
    Tree.delete()
    angle = float(angle) * (pi / 180)
    Tree.angle = angle
    Tree.generate()

def main():
    global Tree
    global scale
    Tree = tree()
    scale.config(command=update)
main()
win.mainloop()
