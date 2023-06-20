from tkinter import *
from PIL import ImageTk
import datetime



root = Tk()

# Ser Screen Size
root.geometry('1280x690+0+0')
root.resizable(False,False)
root.title("Student BioData Form- DataBase")





Label(root, text="Welcome To DataBase", font=("Calibri", 25, "normal")).place(x=500, y= 10)


root.mainloop()