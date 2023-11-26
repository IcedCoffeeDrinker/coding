from tkinter import *
import pickle
import random
from PIL import ImageTk

# settings
win_height = 350
win_width = 300
bg_color = '#000000'

# window setup
win = Tk()
win.geometry(f'{win_width}x{win_height}')
win.resizable(False, False)
win.title('name trainer')
win.config(bg=bg_color)

# elements
check = Button(win, text='check')
check.pack()
enter_name = Entry(win)
enter_name.pack()
img_label = Label(win)
img_label.pack()
info_label = Label(win)
info_label.pack()
star_box = Checkbutton(win, text='star', onvalue=True, offvalue=False)
star_box.pack()

# vars
with open("student_data.pkl", "rb") as f:
    student_data = pickle.load(f)
wait = False
for name in student_data:
    student_data[name]['star'] = False

# program
def select_image():
    current_person = random.choice(list(student_data.items()))
    show_image(current_person[1]['image'])
    return current_person
    
def show_image(image):
    tk_image = ImageTk.PhotoImage(image)
    img_label.config(image=tk_image)
    img_label.image = tk_image # prevent garbage collection or whatever

current_person = select_image()
info_label.config(text=f'name:{len(current_person[0])*'*'}', fg='white')

def check_star():
    if star_box.get():
        student_data['name']['star'] = True
    else:
        student_data['name']['star'] = False
star_box.config(command=check_star)

def check_entry():
    global wait
    global current_person
    if not wait:
        entered_data = enter_name.get()
        enter_name.delete(0, 'end') 
        state = True if entered_data == current_person[0] else False
        info_label.config(text=f'name: {current_person[0]}, {current_person[1]['form']} ({state})', fg='white')
        wait = True
    else: 
        current_person = select_image()
        info_label.config(text=f'name:{len(current_person[0])*'*'}', fg='white')
        #if star_box.ge
        wait = False
check.config(command=check_entry)


        

win.mainloop()