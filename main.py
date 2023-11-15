from pynput import keyboard
from pynput.keyboard import Controller, Key

keyboard_controller = Controller()
expansions = {
    "brb": "be right back", 
    "omw": "on my way",
    "acmgreen": "Verified that ACM light is green on the TMC. ",
    "acmred": "Verified that ACM light is red on the TMC. ",
    "shoulderl": "Verified that lane is a shoulder lane. Shoulder lanes do not have normal traffic."

    }
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
    if current_word in expansions:
        # Delete the shortcut word
        for _ in range(len(current_word) + 1):
            keyboard_controller.press(Key.backspace)
            keyboard_controller.release(Key.backspace)

        # Type the expanded text
        expanded_text = expansions[current_word]
        keyboard_controller.type(expanded_text)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
