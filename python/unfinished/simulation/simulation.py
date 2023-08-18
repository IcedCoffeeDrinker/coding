from tkinter import *
import time
from numpy import *
import random

# settings
window_size = 500
FPS = 60

#window
win = Tk()
win.title("spiral lol")
win.resizable(False, False)
win.geometry(str(window_size) + "x" + str(window_size))
win.configure(background="#2D3436")

canvas = Canvas(win, width=window_size, height=window_size, bg="#2D3436", highlightthickness=0)
canvas.place(x=0,y=0)

# variables
speed = round(1000/FPS)

# functions
class ball:
    id = 0
    def __init__(self, radius, mass, color, position, velocity, acceleration):
        self.id = ball.id
        ball.id += 1

        self.radius = radius
        self.mass = mass
        self.color = color
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

        self.lastCollisionBall = False

        self.circle = canvas.create_oval(self.position[0]-self.radius, self.position[1]-self.radius, self.position[0]+self.radius, self.position[1]+self.radius, fill=self.color, width=0)

    def collision_wall(self):
        if self.position[0]-self.radius <= 0 or self.position[0]+self.radius >= window_size:
            self.velocity[0] *= -1
        if self.position[1]-self.radius <= 0 or self.position[1]+self.radius >= window_size:
            self.velocity[1] *= -1

    def collision_ball(self):
        for local_ball in balls:
            if local_ball.id != self.id:
                a = abs(self.position[0]-local_ball.position[0])
                b = abs(self.position[1]-local_ball.position[1])
                c = sqrt(a*a+b*b)
                if c <= self.radius+local_ball.radius and self.lastCollisionBall == False:
                    # local_ball = 1, self = 2
                    n = [local_ball.position[0]-self.position[0], local_ball.position[1]-self.position[1]] # 1.
                    un = [n[0]/sqrt(n[0]**2+n[1]**2), n[1]/sqrt(n[0]**2+n[1]**2)]
                    ut = [un[1]*-1, un[0]]

                    v1 = local_ball.velocity # 2.
                    v2 = self.velocity

                    v1n = dot(un, v1) # 3.
                    v1t = dot(ut, v1)
                    v2n = dot(un, v2)
                    v2t = dot(ut, v2)

                    m1 = local_ball.mass # 4.
                    m2 = self.mass
                    v1n = v1n*(m1-m2)+2*m2*v2n/(m1+m2)
                    v2n = v2n*(m2-m1)+2*m1*v1n/(m1+m2)

                    v1n = [un[0]*v1n, un[1]*v1n] # 5.
                    v1t = [ut[0]*v1t, ut[1]*v1t]
                    v2n = [un[0]*v2n, un[1]*v2n]
                    v2t = [ut[0]*v2t, ut[1]*v2t]

                    v1 = [v1n[0]+v1t[0], v1n[1]+v1t[1]] # 6.
                    v2 = [v2n[0]+v2t[0], v2n[1]+v2t[1]]

                    print(self.velocity)
                    #local_ball.velocity = v1
                    self.velocity = v2
                    print(self.velocity)


                    print("collision", a, b, c)
                    self.lastCollisionBall = True
                elif c > self.radius+local_ball.radius:
                    self.lastCollisionBall = False

    def move(self):
        canvas.delete(self.circle)
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.circle = canvas.create_oval(self.position[0]-self.radius, self.position[1]-self.radius, self.position[0]+self.radius, self.position[1]+self.radius, fill=self.color, width=0)

# main
def loop():
    start = time.time()
    for ball in balls:
        ball.collision_wall()
        ball.collision_ball()
    for ball in balls:
        ball.move()
    end = time.time()
    duration = round(end-start)
    win.after(speed-duration, loop)

def randomPoint():
    xy = random.randint(0, window_size)
    return xy

def ballmachine(amount, size):
    for i in range(amount):
        x = randomPoint()
        y = randomPoint()
        local_ball = ball(size, 1, "white", [x,y], [random.randint(0,4),random.randint(0,4)], [0,0])
        balls.append(local_ball)


def main():
    global balls
    balls = []
    #amount = int(input("enter amount: "))
    #radius = float(input("enter radius: "))
    #ballmachine(amount,radius)

    ball1 = ball(30, 1, "white", [100,250], [2.5,0.5], [0,0])
    ball2 = ball(30, 1, "yellow", [400,250], [-2.5,0], [0,0])
    #ball3 = ball(30, 3, "red", [400,150], [2.5,2], [0,0])

    balls.append(ball1)
    balls.append(ball2)
    #balls.append(ball3)

    loop()
main()

win.mainloop()
