from tkinter import *
from tkinter.ttk import *
import time

def start():
    end_at = 10
    currently_at = 0

    bar["value"] = 0
    while currently_at < end_at:
        percent.set(str(int((currently_at / end_at) * 100)) + "%")
        time.sleep(0.2)
        bar["value"] += 5
        currently_at += 0.5
        prog_root.update_idletasks()

    prog_root.destroy()
    import screen1

prog_root = Tk()
prog_root.geometry("400x100+100+100")
prog_root.resizable(False, False)
prog_root.title("Logging in...")

percent = StringVar()

bar = Progressbar(prog_root, orient=HORIZONTAL, length=300, mode='determinate')
bar.pack(pady=20)

percent_label = Label(prog_root, textvariable=percent)
percent_label.pack(pady=10)

start()

prog_root.mainloop()
