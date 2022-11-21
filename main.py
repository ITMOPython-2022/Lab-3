import tkinter as tk
from tkinter import messagebox
from sqrEq import sqr_eq


def close():
    window.destroy()


def calc():
    A = float(arg_A.get())
    B = float(arg_B.get())
    C = float(arg_C.get())
    if A == 0:
        tk.messagebox.showerror('Error', 'Division by zero!')
    else:
        lbl_result.configure(text=sqr_eq(A, B, C))


window = tk.Tk()
window.title('Title')
window.geometry('360x240')
bg = tk.PhotoImage(file='gradient.png')

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_bg = tk.Label(frame, image=bg)
lbl_bg.place(x=0, y=0)

lbl_A = tk.Label(frame, text='A', font=('Arial', 30), bg='#000099', fg='#dddddd')
lbl_A.grid(column=0, row=0, padx=10, pady=15)
arg_A = tk.Entry(frame, width = 10)
arg_A.insert(0, '1')
arg_A.grid(column=0, row=1, padx=10, pady=15)

lbl_B = tk.Label(frame, text='B', font=('Arial', 30))
lbl_B.grid(column=1, row=0, padx=10, pady=15)
arg_B = tk.Entry(frame, width = 10)
arg_B.insert(0, '0')
arg_B.grid(column=1, row=1, padx=10, pady=15)

lbl_C = tk.Label(frame, text='C', font=('Arial', 30))
lbl_C.grid(column=2, row=0, padx=10, pady=15)
arg_C = tk.Entry(frame, width = 10)
arg_C.insert(0, '0')
arg_C.grid(column=2, row=1, padx=10, pady=15)

lbl_roots = tk.Label(frame, text='Result:')
lbl_roots.grid(column=0, row=2)
lbl_result = tk.Label(frame, text='Enter the values.', font=('Arial', 10))
lbl_result.grid(column=2, row=2)

btn_calc = tk.Button(frame, text='Calculate', font=('Arial', 15), command=calc)
btn_calc.grid(column=0, row=3)
btn_exit = tk.Button(frame, text='Cancel', font=('Arial', 15), command=close)
btn_exit.grid(column=2, row=3)

window.mainloop()