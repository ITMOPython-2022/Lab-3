# from tkinter import Tk, PhotoImage, Frame, Label, Entry, Button
from tkinter import *
from sqreq import sqr_eq


def clicked():
    A = float(arg_A.get())
    B = float(arg_B.get())
    C = float(arg_C.get())
    lbl_result.configure(text=sqr_eq(A, B, C))


def close():
    window.destroy()


window = Tk()
window.title("Square equations super solver 3000")
window.geometry('360x250')
bg = PhotoImage(file = "gradient.png")
# window.configure(background='green')

frame = Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='c')

label1 = Label(frame, image=bg)
label1.place(x=0, y=0)

lbl_A = Label(frame, text="A", font=("Arial Bold", 30), bg="#eeeeee")
lbl_A.grid(column=0, row=0, padx=10, pady=20)
arg_A = Entry(frame, width=15)
arg_A.insert(0, '1')
arg_A.grid(column=0, row=1, padx=10, pady=20)

lbl_B = Label(frame, text="B", font=("Arial Bold", 30), bg="#eeeeee")
lbl_B.grid(column=1, row=0, padx=10, pady=20)
arg_B = Entry(frame, width=15)
arg_B.insert(0, '0')
arg_B.grid(column=1, row=1, padx=10, pady=20)

lbl_C = Label(frame, text="C", font=("Arial Bold", 30), bg="#eeeeee")
lbl_C.grid(column=2, row=0, padx=10, pady=20)
arg_C = Entry(frame, width=15)
arg_C.insert(0, '0')
arg_C.grid(column=2, row=1, padx=10, pady=20)

lbl_result = Label(frame, text="ROOTS:", bg="#eeeeee")
lbl_result.grid(column=0, row=2)
lbl_result = Label(frame, text="Enter the values.", bg="#eeeeee")
lbl_result.grid(column=2, row=2)

btn = Button(frame, text="Calculate", font=("Arial Bold", 15), command=clicked)
btn.grid(column=0, row=3, pady=15)
exit = Button(frame, text="Cancel", font=("Arial Bold", 15), command=close)
exit.grid(column=2, row=3, pady=15)

window.mainloop()