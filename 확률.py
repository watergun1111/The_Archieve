from tkinter import *
win = Tk()
win_width, win_height = 640, 540
win.geometry(str(win_width)+"x"+str(win_height))
win.config(bg = "black")

value = 0
condition = 0

def Pf():
    global condition
    pcpih.config(text = "P")
    condition = 1

def Cf():
    global condition
    pcpih.config(text = "C")
    condition = 2

def pif():
    global condition
    pcpih.config(text = "Π")
    condition = 3

def Hf():
    global condition
    pcpih.config(text = "H")
    condition = 4

def fac(num):
    if num >= 1:
        for x in range(num-1, 0, -1):
            num *= x
        return num
    elif num == 0:
        return 1

def equal():
    if condition == 1:
        if int(n.get()) >= int(r.get()):
            value = round(fac(int(n.get())) / fac(int(n.get()) - int(r.get())))
            val.config(text = str(value))
        else:
            val.config(text = "ERROR")
    
    if condition == 2:
        if int(n.get()) >= int(r.get()):
            value = round(fac(int(n.get())) / ((fac(int(n.get()) - int(r.get()))) * fac(int(r.get()))))
            val.config(text = str(value))
        else:
            val.config(text = "ERROR")

    if condition == 3:
        value = round(int(n.get()) ** int(r.get()))
        val.config(text = str(value))

    if condition == 4:
        value = round(fac(int(n.get()) + int(r.get()) - 1) / ((fac(int(n.get()) - 1) * fac(int(r.get())))))
        val.config(text = str(value))
    
def closewindow():
    win.destroy()


win.option_add("*Font", "HY견고딕 160 bold")

pcpih = Label(win, fg = "white", bg = "black")
pcpih.place(x = win_width//2 - 75, y = win_height//2 - 90, width = 180, height = 180)

win.option_add("*Font", "HY견고딕 45 bold")

n = Entry(win, bg = "black", fg = "white")
n.place(x = win_width//2 - 240, y = win_height//2, width = 150, height = 90)

r = Entry(win, bg = "black", fg = "white")
r.place(x = win_width//2 + 120, y = win_height//2, width = 150, height = 90)

equal = Button(win, fg = "white", bg = "black", text = "=", command = equal)
equal.place(x = 30, y = 418, width = 64, height = 64)

win.option_add("*Font", "HY견고딕 15 bold")

val = Label(win, bg = "black", fg = "white", text = "No value", wraplength = 520)
val.place(x = 94, y = 360, width = 546, height = 180)

win.option_add("*Font", "HY견고딕 16 bold")

P_btn = Button(win, fg = "white", bg = "black", text = "nPr", command = Pf)
P_btn.place(x = 0, y = 0, width = 128, height = 80)

C_btn = Button(win, fg = "white", bg = "black", text = "nCr", command = Cf)
C_btn.place(x = 128, y = 0, width = 128, height = 80)

pi_btn = Button(win, fg = "white", bg = "black", text = "nΠr", command = pif)
pi_btn.place(x = 256, y = 0, width = 128, height = 80)

H_btn = Button(win, fg = "white", bg = "black", text = "nHr", command = Hf)
H_btn.place(x = 384, y = 0, width = 128, height = 80)

close_btn = Button(win, fg = "white", bg = "red", text = "X", command = closewindow)
close_btn.place(x = 512, y = 0, width = 128, height = 80)

win.mainloop()