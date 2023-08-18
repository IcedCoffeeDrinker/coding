from pynput.mouse import Controller

my_mouse = Controller()

# get mouse position
while True:
    print(my_mouse.position)