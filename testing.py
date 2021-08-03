import pyautogui as pag
import PIL
import time
from icons import *

if __name__ == '__main__':
    screenSize = pag.size()
    middleX, middleY = screenSize[0] / 2, screenSize[1] / 2

    # time.sleep(3)
    # chromeIcon = pag.position()
    # print(chromeIcon)
    # time.sleep(3)
    # newTab1 = pag.position()
    # print(newTab1)
    # time.sleep(3)
    # wykop = pag.position()
    # print(wykop)
    # time.sleep(1)

    pag.click(chrome)
    pag.click(newTab1, _pause=0.1)
    pag.click(wykop)