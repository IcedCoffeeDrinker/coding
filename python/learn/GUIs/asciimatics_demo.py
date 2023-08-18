from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent

def move_character(screen):
    # Initial position
    x, y = screen.width // 2, screen.height // 2

    while True:
        # Clear the screen
        screen.clear()

        # Draw the character at the current position
        screen.print_at('@', x, y, colour=Screen.COLOUR_GREEN)

        # Refresh the screen
        screen.refresh()

        # Wait for an event (key press)
        event = screen.get_event()

        # Check if the event is a keyboard event
        if isinstance(event, KeyboardEvent):
            if event.key_code == Screen.KEY_UP:
                y -= 1
            elif event.key_code == Screen.KEY_DOWN:
                y += 1
            elif event.key_code == Screen.KEY_LEFT:
                x -= 1
            elif event.key_code == Screen.KEY_RIGHT:
                x += 1
            elif event.key_code == Screen.KEY_ESCAPE:
                # Exit the loop if the Escape key is pressed
                break

# Run the function using asciimatics' Screen wrapper
Screen.wrapper(move_character)
