import tkinter as tk
from tkinter import Button, Frame, Entry, Label, ttk, StringVar

app = tk.Tk()
class App:
	def __init__(self, root):
		self.frameDB = []
		self.entryDB = []
		self.count = 0
		self.root = root
		self.create = Button(self.root, text="Create", command=self.draw)
		self.create.pack(side="bottom")
	def draw(self):
		self.frameDB.append(Frame(self.root, borderwidth=1, relief="solid"))
		self.frameDB[self.count].pack(side="top")

		# Label
		self.fWeaponLabel = tk.Label(self.frameDB[self.count], text="Sword")
		self.fWeaponLabel.grid(row=1, column=1)

		# First Combo
		WeaponInpt1Txt = StringVar(None)
		WeaponInpt1 = ttk.Combobox(self.frameDB[self.count], width=20, textvariable=WeaponInpt1Txt, state='readonly')
		WeaponInpt1['values'] = ('Movement', 'Neutral Heavy', 'Down Heavy', 'Side Heavy', 'Neutral Light', 'Down Light', 'Side Light', 'Recovery', 'Neutral Air', 'Down Air', 'Side Air', 'Jump', 'Dash Jump', 'Fast Fall', 'Dodge up', 'Dodge down', 'Forward Dodge', 'Throw', 'Pickup')
		WeaponInpt1.set('Movement')
		WeaponInpt1.grid(row=1, column=4)

		# Delay Duration
		InputDelay1Txt = StringVar(None)
		InputDelay1 = ttk.Combobox(self.frameDB[self.count], width=5, textvariable=InputDelay1Txt, state='readonly')
		InputDelay1['values'] = ('Delay', 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.15, 0.20, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1)
		InputDelay1.set('Delay')
		InputDelay1.grid(row=1, column=5)

		# # Second Combo
		WeaponInpt2Txt = StringVar(None)
		WeaponInpt2 = ttk.Combobox(self.frameDB[self.count], width=20, textvariable=WeaponInpt2Txt, state='readonly')
		WeaponInpt2['values'] = ('Movement', 'Neutral Heavy', 'Down Heavy', 'Side Heavy', 'Neutral Light', 'Down Light', 'Side Light', 'Recovery', 'Neutral Air', 'Down Air', 'Side Air', 'Jump', 'Dash Jump', 'Fast Fall', 'Dodge up', 'Dodge down', 'Forward Dodge', 'Throw', 'Pickup')
		WeaponInpt2.set('Movement')
		WeaponInpt2.grid(row=1, column=6)

		# Key to use
		ChooseKeyTxt = StringVar(None)
		ChooseKey = ttk.Combobox(self.frameDB[self.count], width=5, textvariable=ChooseKeyTxt, state='readonly')
		ChooseKey['values'] = ('key', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
		ChooseKey.set('key')
		ChooseKey.grid(row=1, column=7)

		self.EnableMacro = tk.Button(self.frameDB[self.count], text="Enable", command=lambda counter=self.count: self.EnableCommand(Mov1=WeaponInpt1Txt.get(), Dly=InputDelay1Txt.get(), Mov2= WeaponInpt2Txt.get(), Key=ChooseKeyTxt.get(), isenable=True, counter=counter))
		self.EnableMacro.grid(row=1, column=9)

		self.DisableMacro = tk.Button(self.frameDB[self.count], text="Disable", command=lambda counter=self.count: self.DisableCommand(Mov1=WeaponInpt1Txt.get(), Dly=InputDelay1Txt.get(), Mov2= WeaponInpt2Txt.get(), Key=ChooseKeyTxt.get(), isenable=False, counter=counter))
		self.DisableMacro.grid(row=1, column=10)

		self.DeleteMacro =  tk.Button(self.frameDB[self.count], text="Delete", command=lambda counter=self.count: self.DeleteCommand(counter))
		self.DeleteMacro.grid(row=1, column=11)

		self.entryDB.append([WeaponInpt1, InputDelay1, WeaponInpt2, ChooseKey])
		self.count += 1
	
	# Enable Button
	def EnableCommand(self, Mov1, Dly, Mov2, Key, isenable, counter):
		for i in self.entryDB[counter]:
			print(i.get())

	# Disable Button
	def DisableCommand(self, Mov1, Dly, Mov2, Key, isenable, counter):
		for i in self.entryDB[counter]:
			print(i.get())

	# Delete Button
	def DeleteCommand(self, counter):
		self.fWeaponLabel.grid_forget()
		self.EnableMacro.grid_forget()
		self.DisableMacro.grid_forget()
		self.DeleteMacro.grid_forget()
		for i in self.entryDB[counter]:
			print(i.grid_forget())

App(app)
app.resizable(width=False, height=False)
app.mainloop()