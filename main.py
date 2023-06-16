from tkinter import *
from PIL import ImageTk


root = Tk()

# Ser Screen Size
root.geometry('1280x690+0+0')
root.resizable(False,False)
root.title("Student BioData Form")

# Load Background image
# bg_img = ImageTk.PhotoImage(file="assets/images/background.jpg")


# PLace the image on the screen
# bg_label = Label(root, image = bg_img)
# bg_label.place(x=0, y=0)

login_frame = Frame(root)
login_frame.place(x=440, y=200)


# Load Student Icon
login_icon = PhotoImage(file="assets/images/studen.png")

student_logo_label = Label(login_frame, image=login_icon)
student_logo_label.grid(row=0, column=0, columnspan=2, pady=10)


username_image = PhotoImage(file="assets/images/profile.png")

username_label = Label(login_frame, image=username_image , text="Username", compound=LEFT, font=('times new roman', 20,"bold"),bg="white")
username_label.grid(row=1, column=0, pady=10, padx=20)

user_name_entry = Entry(login_frame,font=('times new roman', 20,"bold")).grid(row=1, column=1, pady=10, padx=20)

# Password Entry
password_image = PhotoImage(file="assets/images/profile.png")
password_label = Label(login_frame, image=password_image, text="Password", compound=LEFT, font=('times new roman', 20,"bold"),bg="white")
password_label.grid(row=2, column=0, pady=10, padx=20)

password_entry = Entry(login_frame,font=('times new roman', 20,"bold")).grid(row=2, column=1, pady=10, padx=20)




root.mainloop()