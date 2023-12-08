import pyautogui
from time import sleep
import win32api, win32con
import keyboard
from threading import Thread

print("Bot Started")

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def connectionError():
	while True:
		if pyautogui.locateOnScreen("connectionError.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("connectionError.png", grayscale=True, confidence=0.8)
			try:
				click(555, 390);
				sleep(5);
			except TypeError:
				print("A TypeError has been occured: connectionError");


def staminaTabs():
	while True:
		if pyautogui.locateOnScreen("staminaTabs.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("staminaTabs.png", grayscale=True, confidence=0.8)
			try:
				click(520, 385);
				sleep(4);
				click(798, 358);
				sleep(4);
				click(571, 441);
				sleep(4);
				click(671, 378);
				sleep(4);
				click(760, 507);
				sleep(4);
			except TypeError:
				print("A TypeError has been occured: staminaTabs");

if __name__ == '__main__':
    Thread(target = connectionError).start()
    Thread(target = staminaTabs).start()