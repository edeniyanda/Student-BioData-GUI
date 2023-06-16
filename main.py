from tkinter import *
from tkinter import messagebox
from PIL import ImageTk



def login():
    if user_name_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror("Error", "Fields cannot be blank")
    elif user_name_entry.get() == "Eden" and password_entry.get() == "1234":
        messagebox.showinfo("Welcome😊","Sign in Successful")
    else:
        messagebox.showerror("Login Fail", "Invalid username or password")

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

username_label = Label(login_frame, image=username_image , text="Username", compound=LEFT, font=('times new roman', 20,"normal"),bg="white")
username_label.grid(row=1, column=0, pady=10, padx=20)

user_name_entry = Entry(login_frame,font=('times new roman', 20))
user_name_entry.grid(row=1, column=1, pady=10, padx=20)

# Password Entry
password_image = PhotoImage(file="assets/images/padlock.png")
password_label = Label(login_frame, image=password_image, text="Password", compound=LEFT, font=('times new roman', 20,"normal"),bg="white")
password_label.grid(row=2, column=0, pady=10, padx=20)

password_entry = Entry(login_frame,font=('Calibri', 20, "normal"))
password_entry.grid(row=2, column=1, pady=10, padx=20)

# Login Button
login_button = Button(login_frame, text="Login", font=('times new roman', 14), width=27, fg="white", bg="black", cursor="hand2", command=login)
login_button.grid(row=3,column=1, pady=10)


root.mainloop()