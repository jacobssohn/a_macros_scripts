import base64
import pyautogui as pya
import pyperclip

from pynput import keyboard
import pytesseract as pt
pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
from PIL import ImageGrab, Image

def screenshot_reader():
    img1 = ImageGrab.grabclipboard()
    img1 = img1.convert('L')
    img1 = np.array(img1)
    print(type(img1))
    #img1 = cv2.cvtColor(img1.astype('uint8'), cv2.COLOR_BGR2BGRA)
    plt.imshow(img1)
    plt.show()
    # img1 = cv2.medianBlur(img1, 5)
    #_, img1 = cv2.threshold(img1,150,255,cv2.THRESH_BINARY)
    plt.imshow(img1)
    plt.show()
    pyperclip.copy(pt.image_to_string(img1))
    print(pt.image_to_string(img1))
screenshot_reader()


