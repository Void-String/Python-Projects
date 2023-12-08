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

def battleStart():
	while True:
		if pyautogui.locateOnScreen("battleStart.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("battleStart.png", grayscale=True, confidence=0.8)
			try:
				# click(pos.left, pos.top);
				click(731, 484);
				sleep(5);
			except TypeError:
				print("A TypeError has been occured: battleStart");

def solarBeam():
	while True:
		if pyautogui.locateOnScreen("solarBeam.png", grayscale=True, confidence=0.8) != None:
			print("Found Solar Beam is ON: Preparing to attack ...");
			pos = pyautogui.locateOnScreen("solarBeam.png", grayscale=True, confidence=0.8)
			print("Solar Beam: Attack!")
			try:
				# click(pos.left, pos.top)
				click(731, 484);
				sleep(5); 
			except TypeError:
				print("A TypeError has been occured: solarBeam");

def skipDialogue():
	while True:
		if pyautogui.locateOnScreen("skipDialogue.png", grayscale=True, confidence=0.8) != None:
			print("Found Dialogue is ON: Skipping ....");
			try:
				sleep(3)
				click(411, 538)
				sleep(3)
				click(318, 391)
				print("Dialogue Skipped")
				sleep(5); 
			except TypeError:
				print("A TypeError has been occured: solarBeam");

def questClear():
	while True:
		if pyautogui.locateOnScreen("questClear.png", grayscale=True, confidence=0.8) != None:
			print("Quest clear with 3*: Begin next quest ....");
			try:
				sleep(4)
				click(432, 365)
				sleep(4)
				click(538, 537)
				sleep(5)
				click(304, 274)
				sleep(5)
				click(638, 519)
				print("Next quest started")
			except TypeError:
				print("A TypeError has been occured: questClear");

def questUnclear():
	while True:
		if pyautogui.locateOnScreen("questUnclear.png", grayscale=True, confidence=0.8) != None:
			print("Quest not clear with 3*: Try again ....");
			try:
				sleep(3)
				click(689, 526)
				print("Quest started")
			except TypeError:
				print("A TypeError has been occured: questUnclear");


if __name__ == '__main__':
    Thread(target = battleStart).start()
    # Thread(target = solarBeam).start()
    Thread(target = skipDialogue).start()
    Thread(target = questClear).start()
    Thread(target = questUnclear).start()