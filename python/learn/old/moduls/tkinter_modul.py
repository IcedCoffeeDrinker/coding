from tkinter import *

# window
root = Tk()
# change title
root.title("no")
# set window size
# /root.geometry("500x500")

# creating a Label Widgit
widgit = Label(root, text="Hello World!")
# Showing it onto the screen
# /widgit.pack()

# show with grid system (interfears with .pack)
widgit2 = Label(root, text="grid")
widgit3 = Label(root, text="grid2")
# with .grid the widgits are relative to each other and empty colums or rows are ingnored and passed
widgit2.grid(row=0, column=0)
widgit3.grid(row=5, column=0)

# you can use coordinates:
segoodwidgit = Label(root, text="xy")
segoodwidgit.place(x=300,y=300)
# does not expand window

# here you can change font and size (fonts = Courier, Helvetica and Times)
def clicked():
    lulLabel = Label(root, text="Never gona give you up, ...", fg="red", font=("Helvetica", 44))
    lulLabel.grid(row=9, column=0)


# this is a button
# with text="...", state=DISABLED you can disable it
# you can youse padx=... or pady=... or (width and height?)to change it's size
# command can run a function. make shure not to use parentesies
# fg changes the letter color (fg = foreground)
# bg changes the color of the button (bg = background)
# #ffffff works too
lulButton = Button(root, text="lul", padx=50, pady=50, command=clicked, fg="blue", bg="gray")
lulButton.grid(row=8, column=0)

# when you pack something with grid you can use "columnspan=..." so the widgit spans over ... widgits

# mainloop updating?
root.mainloop()

# if you realy want to position something right, use .place(relx=..., rely=..., anchor="center")




# 22.12.2022 add:
##window
#win = Tk()
#win.title("Pi")
#win.resizable(False, False)
#win.geometry(str(window_width) + "x" + str(window_height))
#win.configure(background="#2D3436")
