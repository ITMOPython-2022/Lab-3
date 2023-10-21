import tkinter as tk
from tkinter import messagebox
from sqrEq import sqrEquation


def close():
    window.destroy()


def calc():
    A = float(arg_A.get())
    B = float(arg_B.get())
    C = float(arg_C.get())
    if A == 0.0:
        tk.messagebox.showwarning('Error', 'Division by zero!')
    else:
        lbl_result.configure(text=sqrEquation(A, B, C))


window = tk.Tk()
window.geometry('576x360')
bg_img = tk.PhotoImage(file='bg_pic.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_A = tk.Label(frame, text='A', font=('Arial', 30), bg='blue', fg='white')
lbl_A.grid(column=0, row=0, padx=10, pady=15)
arg_A = tk.Entry(frame, width=10)
arg_A.insert(0, '1')
arg_A.grid(column=0, row=1, padx=10, pady=15)

lbl_B = tk.Label(frame, text='B', font=('Arial', 30))
lbl_B.grid(column=1, row=0, padx=10, pady=15)
arg_B = tk.Entry(frame, width=10)
arg_B.insert(0, '0')
arg_B.grid(column=1, row=1, padx=10, pady=15)

lbl_C = tk.Label(frame, text='C', font=('Arial', 30))
lbl_C.grid(column=2, row=0, padx=10, pady=15)
arg_C = tk.Entry(frame, width=10)
arg_C.insert(0, '0')
arg_C.grid(column=2, row=1, padx=10, pady=15)

lbl_roots = tk.Label(frame, text='Result:')
lbl_roots.grid(column=1, row=2)
lbl_result = tk.Label(frame, text='None yet.', font=('Arial', 10))
lbl_result.grid(column=2, row=2)

btn_calc = tk.Button(frame, text='Calculate', command=calc)
btn_calc.grid(column=0, row=3, padx=10, pady=15)
btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.grid(column=2, row=3, padx=10, pady=15)


window.mainloop()