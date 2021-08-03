import base64
import pyautogui as pya
import pyperclip
from pynput import keyboard
import pytesseract
import cv2
import time

# your_code = base64.b64encode(b"""


print('Written by Jakub Rajs, all rights reserved. '
      'I hope this makes your life easier!')

class Clipboard:
    '''
        Class storing the copied text, consisting of two functions - copy and paste.

        Copy:
            No inputs and no returns, it may execute faster than the actual CTRL + C windows function,
            hence time.sleep.

        Paste:
            No inputs and no returns, it only types in the self.text parameter. If the hotkey uses CTRL,
            it's necessary to use the pya.press to reset CTRL button, otherwise it'll be pressed while typing.
    '''
    def __init__(self):
        pass

    def copy_text(self) -> None:
        pya.hotkey('ctrl', 'c')
        time.sleep(.1)
        self.text = pyperclip.paste()

    def paste_text(self) -> None:
        pya.press('ctrl') # comment if the paste hotkey doesn't use CTRL key
        pya.typewrite(self.text)



'''Non OOP take with global variable instead.'''
# #MESSAGE = ''
# def copy_f():
#     pya.hotkey('ctrl', 'c')
#     time.sleep(.1)
#     global MESSAGE
#     MESSAGE = pyperclip.paste()
#
# def paste_f():
#     pya.press('alt')
#     pya.press('shift')
#     pya.typewrite(MESSAGE)

if __name__ == '__main__':

    clip = Clipboard()

    '''Non OOP version uses the lines below'''
    # copy_hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<f1>'), copy_f)
    # paste_hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<f4 >'), paste_f)

    '''Important notes on choosing hotkeys:
        -if character keys are used, make sure they are used with a modifier that turns off typing, e.g. CTRL
        -CTRL will make typed characters be used as hotkeys in other apps, so remember the line in paste_text
        -lots of hotkeys are in use in various apps, I don't think it's possible to consider all of them so errors are okay
        -keys shouldn't be too far apart, duh
    '''
    # copy_hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<f1>'), clip.copy_text) # you can change the hotkeys here
    # paste_hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<f2>'), clip.paste_text)# and here
    
    copy_hotkey = keyboard.HotKey(keyboard.HotKey.parse('<alt>+<shift>+q'), clip.copy_text) # you can change the hotkeys here
    paste_hotkey = keyboard.HotKey(keyboard.HotKey.parse('<alt>+<shift>+s'), clip.paste_text)# and here
    hotkeys = [copy_hotkey, paste_hotkey]

    def on_press(key):
        for hotkey in hotkeys:
            hotkey.press(listener.canonical(key))

    def on_release(key):
        for hotkey in hotkeys:
            hotkey.release(listener.canonical(key))

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# Property of Jakub Rajs, all rights reserved

# """)
#
# exec(base64.b64decode(your_code))