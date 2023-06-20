from tkinter import *
from tkinter.ttk import *
import time


root = Tk()

root.geometry("400x100")
root.resizable(False, False)
root.title("Logining in...")


def start():
    end_at = 10
    currently_at = 0
    
    while (currently_at < end_at):
        time.sleep(0.5)
        # bar["value"] += 10
        percent.set(str((currently_at/end_at)*100) + "%")
        currently_at +=1
        root.update_idletasks()
    root.destroy()
    
percent = StringVar()
 
bar = Progressbar(root,orient=HORIZONTAL, length=300)
bar.pack(pady=20)

percent_label = Label(root, text="yo")
percent_label.pack(pady=100)

# start()

root.mainloop()
