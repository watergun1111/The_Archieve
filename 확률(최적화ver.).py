from tkinter import *

win = Tk()
win_width, win_height = 640, 540
win.geometry(f"{win_width}x{win_height}")
win.config(bg="black")

condition = 0

def set_condition(value):
    global condition
    condition = value
    pcpih.config(text=value_mapping[value])

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

def calculate():
    try:
        n_val = int(n.get())
        r_val = int(r.get())

        if condition == 1:
            value = round(factorial(n_val) / factorial(n_val - r_val))
        elif condition == 2:
            value = round(factorial(n_val) / (factorial(n_val - r_val) * factorial(r_val)))
        elif condition == 3:
            value = round(n_val ** r_val)
        elif condition == 4:
            value = round(factorial(n_val + r_val - 1) / (factorial(n_val - 1) * factorial(r_val)))
        else:
            value = "ERROR"

        val.config(text=str(value))
    except ValueError:
        val.config(text="ERROR")

def close_window():
    win.destroy()

value_mapping = {1: "P", 2: "C", 3: "Π", 4: "H"}

win.option_add("*Font", "HY견고딕 160 bold")

pcpih = Label(win, fg="white", bg="black")
pcpih.place(x=win_width // 2 - 75, y=win_height // 2 - 90, width=180, height=180)

win.option_add("*Font", "HY견고딕 45 bold")

n = Entry(win, bg="black", fg="white")
n.place(x=win_width // 2 - 240, y=win_height // 2, width=150, height=90)

r = Entry(win, bg="black", fg="white")
r.place(x=win_width // 2 + 120, y=win_height // 2, width=150, height=90)

equal = Button(win, fg="white", bg="black", text="=", command=calculate)
equal.place(x=30, y=418, width=64, height=64)

win.option_add("*Font", "HY견고딕 15 bold")

val = Label(win, bg="black", fg="white", text="No value", wraplength=520)
val.place(x=94, y=360, width=546, height=180)

win.option_add("*Font", "HY견고딕 16 bold")

buttons_info = [
    {"text": "nPr", "command": lambda: set_condition(1)},
    {"text": "nCr", "command": lambda: set_condition(2)},
    {"text": "nΠr", "command": lambda: set_condition(3)},
    {"text": "nHr", "command": lambda: set_condition(4)},
]

for i, info in enumerate(buttons_info):
    btn = Button(win, fg="white", bg="black", text=info["text"], command=info["command"])
    btn.place(x=i * 128, y=0, width=128, height=80)

close_btn = Button(win, fg="white", bg="red", text="X", command=close_window)
close_btn.place(x=512, y=0, width=128, height=80)

win.mainloop()