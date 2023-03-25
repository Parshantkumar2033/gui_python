from tkinter import *
root = Tk()

#creating entry widget
e = Entry(root) #we can change the color or the size of the space and many more
e.pack()
e.insert(0, "Enter the text : ")      #insert(indexEntry, string)


def click():
    myLabel = Label(root, text = e.get())
    myLabel.pack()

button = Button(root, text = "click", fg = "blue", command = click)
button.pack()

root.mainloop()