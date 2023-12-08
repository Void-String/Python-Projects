import pyautogui
from time import sleep
import win32api, win32con
import keyboard
from threading import Thread
from click import Cancel

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print("Cancel Modules Imported")


def ClickBtn():
    while True:
        if pyautogui.locateOnScreen("Cancel.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("Cancel.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: Cancel");