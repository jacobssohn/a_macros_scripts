import pyautogui as pya
from pynput import mouse


def on_click(x, y, button, pressed):
    with open("icons.py", "a") as f:
        if button == mouse.Button.right:
            name = pya.prompt('This lets the user type in a string and press OK.')
            print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))
            f.write(f"{name} = {x}, {y}\n")
        elif button == mouse.Button.left:
            pass
        else: return False



if __name__ == '__main__':
    listener = mouse.Listener(on_click=on_click)

    listener.start()
    listener.join()
