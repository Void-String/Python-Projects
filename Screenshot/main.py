import pyautogui
from time import sleep


def takeScreenshot():
	sleep(2)
	im1 = pyautogui.screenshot()
	im1.save(r"./savedimage.png")

takeScreenshot()