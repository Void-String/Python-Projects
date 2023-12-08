import pyautogui

print("Press Ctrl-C to set flag")
while True:
	mouse = pyautogui.displayMousePosition()
	print(mouse)