
import time
from math import *
from tkinter import *
import matplotlib.pyplot as plt
from datetime import datetime

#window
window = Tk()
window.title("2b2t queue")
window.resizable(False, False)
window.geometry("500x500")
window.configure(background="#101010")

WindowTitle = Label(window, text="2b2t queue", font=("Helvetica", 30), bg="#101010", fg="white")
WindowTitle.place(x=150, y=0)

WindowPlaceInQueue = Label(window, text="Place in queue:", font=("Helvetica", 20), bg="#101010", fg="white")
WindowPlaceInQueueNumber = Label(window, text="wait", font=("Helvetica", 20), bg="#101010", fg="white")
WindowPlaceInQueue.place(x=150, y=100)
WindowPlaceInQueueNumber.place(x=200, y=150)


WindowMovedPlaces = Label(window, text="Moved Places:", font=("Helvetica", 20), bg="#101010", fg="white")
WindowMovedPlacesNumber = Label(window, text="wait", font=("Helvetica", 20), bg="#101010", fg="white")
WindowMovedPlaces.place(x=150, y=220)
WindowMovedPlacesNumber.place(x=200, y=270)


WindowTimeLeft = Label(window, text="Time left:", font=("Helvetica", 20), bg="#101010", fg="white")
WindowTimeLeftNumber = Label(window, text="wait", font=("Helvetica", 20), bg="#101010", fg="white")
WindowTimeLeft.place(x=150, y=340)
WindowTimeLeftNumber.place(x=175, y=390)

# blotting
plt.title("2b2t queue")
plt.xlabel("time")
plt.ylabel("place in queue")
x = []
y = []

def check ():
    with open(r"\Users\MSI Gaming\AppData\Roaming\.minecraft\logs\latest.log") as file:
        for line in file:
            pass
        last_line = line
        print(last_line)
        file.close()

    posOFpos = last_line.index("Position in queue: ") + len("Position in queue: ")
    number = ""
    for i in range(3):
        digit = last_line[posOFpos+i]
        try:
            int(digit)
            number += digit
        except:
            pass

    print("number:" + number)
    return int(number)

TimeStart = time.time()
FirstRound = True

PlaceInQueue = 100
FirstPlace = 100
TimeLeft = 100
def loop():
    global FirstRound
    global PlaceInQueue
    global FirstPlace
    global TimeLeft
    global x
    global y
    try:
        PlaceInQueue = check()
        print("place in queue: ", PlaceInQueue)
    except:
        print("place in queue: not a number")

    if FirstRound:
        print("First round")
        FirstPlace = PlaceInQueue
        FirstRound = False
        x.append(datetime.now())
        y.append(PlaceInQueue)
        plt.plot(x,y)
        plt.pause(0.05)

    if PlaceInQueue != FirstPlace - PlaceInQueue:
        MovedPlaces = floor(FirstPlace - PlaceInQueue)
        x.append(datetime.now())
        y.append(PlaceInQueue)
        plt.plot(x,y)
        plt.pause(0.05)
    print("moved places: ", MovedPlaces)

    try:
        TimePassed = time.time() - TimeStart
        TimeLeft = TimePassed / MovedPlaces * PlaceInQueue
        TimeLeft = floor(TimeLeft / 60)
        Hour = floor(TimeLeft / 60)
        Minute = TimeLeft - Hour * 60
        FinalTimeLeft = str(Hour) + "h " + str(Minute) + "m"
        print("time left: ", FinalTimeLeft)
    except ZeroDivisionError:
        print("time left: Pls wait!")

    #window
    #global WindowPlaceInQueueNumber
    #global WindowMovedPlacesNumber
    #global WindowTimeLeftNumber

    WindowPlaceInQueueNumber.config(text=PlaceInQueue)
    WindowMovedPlacesNumber.config(text=MovedPlaces)
    if MovedPlaces == 0:
        WindowTimeLeftNumber.config(text="Pls wait!")
    else:
        WindowTimeLeftNumber.config(text=FinalTimeLeft)

    print("-----------------------------------------")
    window.after(10000, loop)





window.after(1000, loop)
window.mainloop()
plt.show()
