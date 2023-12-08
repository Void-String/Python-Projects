import tkinter as tk  
from tkinter import ttk


# Window
app = tk.Tk() # Application Name  
app.title("Discord Rich Presence") # Label
app.geometry("290x500") # Size

# Label
label_uid = ttk.Label(app, text = "ID:")# Click event  
label_uid.place(x=5, y=5)

label_state = ttk.Label(app, text = "State:")# Click event  
label_state.place(x=5, y=50)

label_details = ttk.Label(app, text = "Details:")# Click event  
label_details.place(x=5, y=95) # +45

label_LImage = ttk.Label(app, text = "Large Image:")# Click event  
label_LImage.place(x=5, y=140) # +45

label_SImage = ttk.Label(app, text = "Small Image:")# Click event  
label_SImage.place(x=5, y=185) # +45

label_LImageT = ttk.Label(app, text = "Large Image Tooltip:")# Click event  
label_LImageT.place(x=5, y=230) # +45

label_SImageT = ttk.Label(app, text = "Small Image Tooltip:")# Click event  
label_SImageT.place(x=5, y=275) # +45

# Click event
def CMDUid():
    print(uid.get()) # Textbox widget 
def CMDStatus():   
    print(state.get()) # Textbox widget 
def CMDDetails():
    print(details.get()) # Textbox widget 
def CMDLimage():
    print(limage.get()) # Textbox widget 
def CMDSimage():
    print(simage.get()) # Textbox widget 
def CMDLimageT():
    print(limaget.get()) # Textbox widget 
def CMDSimageT():
    print(simaget.get()) # Textbox widget 

# Widget text box 
uid = tk.StringVar() 
uidEntered = ttk.Entry(app, width = 30, textvariable = uid) 
uidEntered.place(x=5, y=25)

state = tk.StringVar() 
stateEntered = ttk.Entry(app, width = 30, textvariable = state) 
stateEntered.place(x=5, y=70)

details = tk.StringVar() 
detailsEntered = ttk.Entry(app, width = 30, textvariable = details) 
detailsEntered.place(x=5, y=115) # +45

limage = tk.StringVar() 
limageEntered = ttk.Entry(app, width = 30, textvariable = limage) 
limageEntered.place(x=5, y=160) # +45

simage = tk.StringVar() 
simageEntered = ttk.Entry(app, width = 30, textvariable = simage) 
simageEntered.place(x=5, y=205) # +45

limaget = tk.StringVar() 
limagetEntered = ttk.Entry(app, width = 30, textvariable = limaget) 
limagetEntered.place(x=5, y=250) # +45

simaget = tk.StringVar() 
simagetEntered = ttk.Entry(app, width = 30, textvariable = simaget) 
simagetEntered.place(x=5, y=295) # +45

# Buttons position
SetUid = ttk.Button(app, text = "Set", command = CMDUid)
SetUid.place(x=210, y=23)

SetState = ttk.Button(app, text = "Set", command = CMDStatus)
SetState.place(x=210, y=69)

SetDetail = ttk.Button(app, text = "Set", command = CMDDetails)
SetDetail.place(x=210, y=113) # +46

SetLImage = ttk.Button(app, text = "Set", command = CMDLimage)
SetLImage.place(x=210, y=156) # +43

SetSImage = ttk.Button(app, text = "Set", command = CMDSimage)
SetSImage.place(x=210, y=199) # +43

SetLImageT = ttk.Button(app, text = "Set", command = CMDLimageT)
SetLImageT.place(x=210, y=242) # +43

SetSImageT = ttk.Button(app, text = "Set", command = CMDSimageT)
SetSImageT.place(x=210, y=285) # +43

ExitButton= ttk.Button(app, text="Exit", command=app.quit)
ExitButton.pack(side=tk.BOTTOM, padx=5, pady=5)

app.mainloop()