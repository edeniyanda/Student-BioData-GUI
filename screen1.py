from tkinter import *
from PIL import ImageTk
import datetime



screen1_wimdow = Tk()

# Ser Screen Size
screen1_wimdow.geometry('1280x690+0+0')
screen1_wimdow.resizable(False,False)
screen1_wimdow.title("Student BioData Form- DataBase")





Label(screen1_wimdow, text="Welcome To DataBase", font=("Calibri", 25, "normal")).place(x=500, y= 10)


screen1_wimdow.mainloop()