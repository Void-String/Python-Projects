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

def Cancel():
    while True:
        if pyautogui.locateOnScreen("Cancel.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("Cancel.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: Cancel");

def DialogueS():
    while True:
        if pyautogui.locateOnScreen("DialogueS.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("DialogueS.png", grayscale=True, confidence=0.8);
            try:
                click(705, 530);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: DialogueS");

def EnterM():
    while True:
        if pyautogui.locateOnScreen("EnterM.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("EnterM.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: EnterM");

def GuestP():
    while True:
        if pyautogui.locateOnScreen("GuestP.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("GuestP.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: GuestP");

def MissionC():
    while True:
        if pyautogui.locateOnScreen("MissionC.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("MissionC.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: MissionC");

def NextM():
    while True:
        if pyautogui.locateOnScreen("NextM.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("NextM.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: NextM");

def SkipB():
    while True:
        if pyautogui.locateOnScreen("SkipB.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("SkipB.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: SkipB");

def StartM():
    while True:
        if pyautogui.locateOnScreen("StartM.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("StartM.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: StartM");

def YesB():
    while True:
        if pyautogui.locateOnScreen("YesB.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("YesB.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: YesB");

def SolarB():
    while True:
        if pyautogui.locateOnScreen("SolarB.png", grayscale=True, confidence=0.8) != None:
            pos = pyautogui.locateOnScreen("SolarB.png", grayscale=True, confidence=0.8);
            try:
                click(pos.left, pos.top);
                sleep(5000)
            except TypeError:
                print("A TypeError has been occured: SolarB");

if __name__ == '__main__':
	Thread(target = Cancel).start();
	Thread(target = DialogueS).start();
	Thread(target = EnterM).start();
	Thread(target = GuestP).start();
	Thread(target = MissionC).start();
	Thread(target = NextM).start();
	Thread(target = SkipB).start();
	Thread(target = StartM).start();
	Thread(target = YesB).start();
	Thread(target = SolarB).start();
