from asciimatics.screen import Screen
import time

def demo(screen):
    width = screen.width
    height = screen.height
    screen.print_at(f'Terminal width: {width}, height: {height}', 0, 0)
    screen.refresh()
    time.sleep(.1)
    demo(screen)

Screen.wrapper(demo)
