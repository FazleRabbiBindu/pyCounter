# simple counter

import ttkbootstrap as tkb
from ttkbootstrap.constants import *

root = tkb.Window(minsize=(300,200), title="Count!")

#variables
fontName = "Terminal"
count = 0
fontSize = 24


#frame
topFrame = tkb.Frame(root)

# fucntions

def increment(i):
    return i+1

def decrement(d):
    return d-1

def counter(a, btnFlag):
    if btnFlag==1:
        a = increment(a)
    elif btnFlag==2:
        a = decrement(a)
    else:
        a = 0
    return a

def updateCounter(btnFlag):
    global count
    count = counter(count, btnFlag)
    if count < 0:
        count = 0
        
    counterDisplay.config(text=str(count))


# elements
counterDisplay = tkb.Label(
    topFrame,
    anchor="center",
    name="counterDisplay", 
    text= count, 
    font=(str(fontName),fontSize),
    justify="center", 
    bootstyle="inverse-primary")

incrementButton = tkb.Button(
    topFrame,
    bootstyle="success",
    command=lambda: updateCounter(1),
    )

decrementButton = tkb.Button(
    topFrame,
    bootstyle="danger",
    command=lambda: updateCounter(2),
    )

resetButton = tkb.Button(
    root,
    bootstyle="warning",
    command=lambda: updateCounter(3),
    )

#pack
topFrame.pack(side="top", fill=BOTH, expand=True)

incrementButton.pack(side="left", fill=BOTH, padx=5, pady=5, expand=True)
counterDisplay.pack(side="left", fill=BOTH, padx=5, pady=5, expand=True)
decrementButton.pack(side="left", fill=BOTH, padx=5, pady=5, expand=True)
resetButton.pack(side="bottom", fill=BOTH, padx=5, pady=5, expand=True)


#run main loop
root.mainloop()
