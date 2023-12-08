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

def partySelection():
	while True:
		if pyautogui.locateOnScreen("partySelection.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("partySelection.png", grayscale=True, confidence=0.8)
			try:
				print("Searching for a party member ....")
				click(280, 255);
				print("Done")
				sleep(3);
			except TypeError:
				print("A TypeError has been occured: partySelection");

def startQuest():
	while True:
		if pyautogui.locateOnScreen("startQuest.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("startQuest.png", grayscale=True, confidence=0.8)
			try:
				print("Looking for a start button ....")
				click(560, 500);
				print("Done")
				sleep(3);
			except TypeError:
				print("A TypeError has been occured: startQuest");

def questDialogue():
	while True:
		if pyautogui.locateOnScreen("questDialogue.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("questDialogue.png", grayscale=True, confidence=0.8)
			try:
				print("Skipping dialogue ....")
				click(396, 540);
				sleep(3);
				click(294, 404);
				print("Done")
				sleep(3);
			except TypeError:
				print("A TypeError has been occured: questDialogue");

def startButton():
	while True:
		if pyautogui.locateOnScreen("startButton.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("startButton.png", grayscale=True, confidence=0.8)
			try:
				print("Starting a battle ...")
				click(715, 490);
				print("Done")
				sleep(5);
			except TypeError:
				print("A TypeError has been occured: startButton");

def questClear():
	while True:
		if pyautogui.locateOnScreen("questClear.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("questClear.png", grayscale=True, confidence=0.8)
			try:
				print("Quest clear with 3*, begin next quest ... ")
				click(500, 525);
				sleep(3);
				click(500, 525);
				sleep(3);
			except TypeError:
				print("A TypeError has been occured: questClear");

def solarBeam():
	while True:
		if pyautogui.locateOnScreen("solarBeam.png", grayscale=True, confidence=0.8) != None:
			pos = pyautogui.locateOnScreen("solarBeam.png", grayscale=True, confidence=0.8)
			try:
				print("Solar beam is ready, begin to attack ....")
				click(705, 490);
				print("Done")
				sleep(3);
			except TypeError:
				print("A TypeError has been occured: solarBeam");

if __name__ == '__main__':
    Thread(target = partySelection).start()
    Thread(target = startQuest).start()
    Thread(target = questDialogue).start()
    Thread(target = startButton).start()
    Thread(target = questClear).start()
    Thread(target = solarBeam).start()
