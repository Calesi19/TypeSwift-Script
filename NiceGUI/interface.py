from nicegui import ui
from pynput import keyboard
from pynput.keyboard import Controller, Key

# Your keyboard controller and expansions dictionary
keyboard_controller = Controller()
expansions = {
    "brb": "be right back",
    "omw": "on my way",
    # ... other shortcuts
}

# Function to add a new shortcut
def add_shortcut(sender):
    expansions[shortcut.value] = expansion.value
    update_shortcuts_view()
    shortcut.value = ''
    expansion.value = ''

# Function to remove a shortcut
def remove_shortcut(key):
    del expansions[key]
    update_shortcuts_view()

# Function to update the list of shortcuts in the UI
def update_shortcuts_view():
    shortcuts_view.clear()
    for key, value in expansions.items():
        row = shortcuts_view.add_slot(name="wo")
        row.label(f'{key}: {value}')
        row.add_button('Delete', lambda e, key=key: remove_shortcut(key)).style('margin-left: auto')

# UI layout
ui.label('Manage Keyboard Shortcuts')
shortcut = ui.input(label='Shortcut', placeholder='Enter shortcut...')
expansion = ui.input(label='Expansion', placeholder='Enter expansion...')
ui.button('Add', on_click=add_shortcut)

shortcuts_view = ui.column()

# Initial view update
update_shortcuts_view()

ui.run()
