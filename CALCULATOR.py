from tkinter import *
from PIL import Image, ImageTk

def btnclick(number):
    global a
    a += str(number)
    textinput.set(a)

def delete():
    global a
    a = a[:-1]
    textinput.set(a)

def clear():
    global a
    a = ""
    textinput.set(a)

def cal():
    global a
    res = str(eval(a))
    textinput.set(res)

window = Tk()
window.title("Calculator")
window.geometry("400x700")

a = ""

image = Image.open(r"C:\Users\LENOVO\Downloads\logo.png")
image = image.resize((180, 150))
img = ImageTk.PhotoImage(image)
lbl = Label(window, image=img)
lbl.pack(pady=30)

textinput = StringVar()
display = Entry(
    window,
    width=30,
    font=("Arial", 20, "bold"),
    textvariable=textinput,
    bd=30,
    insertwidth=4,
    justify="right"
)
display.pack()

bt7 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="7", command=lambda: btnclick(7))
bt7.place(x=0, y=310)
bt8 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="8", command=lambda: btnclick(8))
bt8.place(x=102, y=310)
bt9 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="9", command=lambda: btnclick(9))
bt9.place(x=204, y=310)
bta = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="/", bg="silver", command=lambda: btnclick("/"))
bta.place(x=306, y=310)

bt4 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="4", command=lambda: btnclick(4))
bt4.place(x=0, y=380)
bt5 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="5", command=lambda: btnclick(5))
bt5.place(x=102, y=380)
bt6 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="6", command=lambda: btnclick(6))
bt6.place(x=204, y=380)
btb = Button(window, padx=23, bd=8, font=("Arial", 20, "bold"),
text="*", bg="silver", command=lambda: btnclick("*"))
btb.place(x=306, y=380)

bt1 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="1", command=lambda: btnclick(1))
bt1.place(x=0, y=450)
bt2 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="2", command=lambda: btnclick(2))
bt2.place(x=102, y=450)
bt3 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="3", command=lambda: btnclick(3))
bt3.place(x=204, y=450)
btc = Button(window, padx=24, bd=8, font=("Arial", 20, "bold"),
text="-", bg="silver", command=lambda: btnclick("-"))
btc.place(x=306, y=450)

btdel = Button(window, padx=5, bd=8, font=("Arial", 20, "bold"),
text="DEL", bg="gray", command=delete)
btdel.place(x=0, y=520)
btpoint = Button(window, padx=29, bd=8, font=("Arial", 20, "bold"),
text=".", command=lambda: btnclick("."))
btpoint.place(x=102, y=520)
bt0 = Button(window, padx=25, bd=8, font=("Arial", 20, "bold"),
text="0", command=lambda: btnclick(0))
bt0.place(x=204, y=520)
btd = Button(window, padx=21, bd=8, font=("Arial", 20, "bold"),
text="+", bg="silver", command=lambda: btnclick("+"))
btd.place(x=306, y=520)

btC = Button(window, padx=22, bd=8, font=("Arial", 20, "bold"),
text="C", bg="gray", command=clear)
btC.place(x=0, y=590)
bte = Button(window, padx=29, bd=8, font=("Arial", 20, "bold"),
text="(", command=lambda: btnclick("("))
bte.place(x=102, y=590)
btf = Button(window, padx=29, bd=8, font=("Arial", 20, "bold"),
text=")", command=lambda: btnclick(")"))
btf.place(x=204, y=590)
btcal = Button(window, padx=21, bd=8, font=("Arial", 20, "bold"),
text="=", bg="red", command=cal)
btcal.place(x=306, y=590)

window.mainloop()