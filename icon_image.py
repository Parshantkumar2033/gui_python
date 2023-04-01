from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("whatsapp")
root.iconbitmap('download.ico')

button_exit = Button(root, text = "Exit", borderwidth= 3, command = root.quit)
button_exit.pack()

image = ImageTk.PhotoImage(Image.open('katakuri.png'))
new_label = Label(image = image)
new_label.pack()


root.mainloop()