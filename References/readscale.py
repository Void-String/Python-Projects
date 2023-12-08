from tkinter import *
master = Tk()
scales=list()
Nscales=10
for i in range(Nscales):
    w=Scale(master, from_=0, to=100) # creates widget
    w.pack(side=RIGHT) # packs widget
    scales.append(w) # stores widget in scales list
def read_scales():
    for i in range(Nscales):
        print("Scale %d has value %d" %(i,scales[i].get()))
b=Button(master,text="Read",command=read_scales) # button to read values
b.pack(side=RIGHT)
mainloop()