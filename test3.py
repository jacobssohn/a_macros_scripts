from pynput import keyboard
def on_hotkey_a():
    print('Hot key A pressed!')

def on_hotkey_b():
    print('Hot key B pressed!')

HOTKEYS = [
    keyboard.HotKey(keyboard.HotKey.parse('<alt>+b'), on_hotkey_a),
    keyboard.HotKey(keyboard.HotKey.parse('<shift>+b'), on_hotkey_b)]

def on_press(key):
    for hotkey in HOTKEYS:
        hotkey.press(l.canonical(key))
    # Handle pressed keys


def on_release(key):
    for hotkey in HOTKEYS:
        hotkey.release(l.canonical(key))
    # Handle released keys


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as l:
    l.join()