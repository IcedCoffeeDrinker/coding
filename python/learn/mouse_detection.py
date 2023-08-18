import tkinter

win = tkinter.Tk()
frame = tkinter.Frame(width=100, height=100, background="bisque")
frame.pack(padx=100, pady=100)
def pressing(event):
    print( "frame coordinates: %s/%s" % (event.x, event.y))
    print( "root coordinates: %s/%s" % (event.x_root, event.y_root))
frame.bind("<1>", pressing)
win.mainloop()
