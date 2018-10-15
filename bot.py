from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (481,508)
    dinosaur = (187,525)
    #280,539

def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box = (Cordinates.dinosaur[0]+60,Cordinates.dinosaur[1],
           Cordinates.dinosaur[0]+190,Cordinates.dinosaur[1]+14)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if imageGrab() != 2067:
            pressSpace()
            time.sleep(0.001)

main()