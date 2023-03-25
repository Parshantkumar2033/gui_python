from tkinter import *
root = Tk()

# button = Button(root, text = "Click here", state = DISABLED)

def click():
    myLabel = Label(root, text = "Clicked the Button")
    myLabel.pack()
#customise the size of button
button = Button(root, text = "Click here", padx = 50, command= click, fg= "blue", bg = "")
button.pack()
root.mainloop()