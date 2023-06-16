from tkinter import *
from PIL import ImageTk


root = Tk()

root.geometry('1280x690+0+0')
root.resizable(False,False)


bg_img = ImageTk.PhotoImage(file="assets/images/background.jpg")


bg_label = Label(root, image = bg_img)
bg_label.place(x=0, y=0)


root.mainloop()