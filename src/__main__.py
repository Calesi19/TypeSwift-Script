from pynput import keyboard
from pynput.keyboard import Controller, Key
import json
import os

keyboard_controller = Controller()

# Load expansions from a JSON file
dir_path = os.path.dirname(os.path.realpath(__file__))
shortcuts_file = os.path.join(dir_path, 'shortcuts.json')

with open(shortcuts_file, 'r') as file:
    expansions = json.load(file)

current_word = ""  # To keep track of the currently typed word

def on_press(key):
    global current_word

    try:
        # Detect alphanumeric key presses
        if hasattr(key, 'char') and key.char:
            if key.char.isalnum():
                current_word += key.char
            elif key.char == ' ':
                replace_word()
                current_word = ""
        elif key == Key.space:
            replace_word()
            current_word = ""
        elif key == Key.backspace:
            current_word = current_word[:-1]  # Remove last character on backspace

    except AttributeError:
        pass

def replace_word():
    global current_word
    if current_word in expansions:
        # Delete the shortcut word
        for _ in range(len(current_word) + 1):
            keyboard_controller.press(Key.backspace)
            keyboard_controller.release(Key.backspace)

        # Type the expanded text
        expanded_text = expansions[current_word]
        keyboard_controller.type(expanded_text)

def main():
    # Starting the keyboard listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()