from tkinter import Label, Entry, StringVar, ttk 
import tkinter as tk


app = tk.Tk()

# Remove and Add Placeholder
class EntryWithPlaceholder(Entry):
    def __init__(self, *args, **kwargs):
        self.placeholder = kwargs.pop("placeholder", "")
        super().__init__(*args, **kwargs)

        self.insert("end", self.placeholder)
        self.bind("<FocusIn>", self.remove_placeholder)
        self.bind("<FocusOut>", self.add_placeholder)

    def remove_placeholder(self, event):
        """Remove placeholder text, if present"""
        if self.get() == self.placeholder:
            self.delete(0, "end")

    def add_placeholder(self,event):
        """Add placeholder text if the widget is empty"""
        if self.placeholder and self.get() == "":
            self.insert(0, self.placeholder)


def CType0Cmd():
	print(str(CType0Text.get()))
def CType1Cmd():
	print(str(CType1Text.get()))


# Label
CType0 = Label(app, text="Unarmed")
CType0.grid(row=1,column=1)

CType1 = Label(app, text="Unarmed")
CType1.grid(row=2,column=1)

# Input Box
CType0Text	=	StringVar(None)
CType0Input	=	EntryWithPlaceholder(app, width=30, placeholder="Address", textvariable=CType0Text)
CType0Input.grid(row=1,column=2)

CType1Text	=	StringVar(None)
CType1Input	=	EntryWithPlaceholder(app, width=30, placeholder="Address", textvariable=CType1Text)
CType1Input.grid(row=2,column=2)

# Button
CType0Button = ttk.Button(app, text = "Activate", command = CType0Cmd)
CType0Button.grid(row=1,column=3)

CType1Button = ttk.Button(app, text = "Activate", command = CType1Cmd)
CType1Button.grid(row=2,column=3)

app.mainloop()