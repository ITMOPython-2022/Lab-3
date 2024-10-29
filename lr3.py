import tkinter as tk
from tkinter import messagebox
import random


def cancel():
    window.destroy()


def turns_countdown():
    global TURNS
    TURNS -= 1
    return TURNS


def guess():
    global WORD_TO_SHOW
    global USED_LETTERS
    letter = letter_entry.get()
    if len(letter) > 1 or letter.isalpha() == False:
        tk.messagebox.showwarning('Неверный ввод!', 'Нужно ввести букву!')
        return 0
    letter = letter.upper()
    letter_entry.delete(-1)
    turns_countdown()
    turns_label.configure(text=f'Осталось ходов: {TURNS}')

    USED_LETTERS += f'{letter} '
    used_letters_label.configure(text=f'Log: {USED_LETTERS}')
    
    if letter in WORD_TO_GUESS:
        word_buf = WORD_TO_SHOW
        WORD_TO_SHOW = ''
        for i in range(5):
            if WORD_TO_GUESS[i] == letter:
                WORD_TO_SHOW += letter
            else:
                WORD_TO_SHOW += word_buf[i]
    #print(WORD_TO_SHOW)
    word_label.configure(text=WORD_TO_SHOW)

    if WORD_TO_SHOW == WORD_TO_GUESS:
        tk.messagebox.showinfo('Победа!', 'Вы угадали слово!')
        window.destroy()

    if TURNS == 0 and WORD_TO_GUESS != WORD_TO_SHOW:
        word_label.configure(text=WORD_TO_GUESS)
        tk.messagebox.showerror('Не победа(', 'Вы не угадали слово...')
        window.destroy()


def word_choose():
    with open('words.txt', 'r') as words_list:
        words = []
        for word in words_list:
            words.append(word)
        myword = random.choice(words)
    return myword


WORD_TO_GUESS = word_choose()[:5]
WORD_TO_SHOW = '*****'
TURNS = 10
USED_LETTERS = ''

window = tk.Tk()
window.title('My app')
window.geometry('300x300')
bg_img = tk.PhotoImage(file='gradient.png')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

word_label = tk.Label(window, text='*****', font=('Consolas', 50), 
                      bg='red', fg='white')
word_label.place(x=0, y=0, relwidth=1)

letter_label = tk.Label(window, text='Введите букву: ', font=('Verdana', 14))
letter_label.place(relx=0.07, rely=0.35)
letter_entry = tk.Entry(window, width=5, font=('Verdana', 16))
letter_entry.insert(0, 'a')
letter_entry.place(relx=0.7, rely=0.35)

turns_label = tk.Label(window, text=f'Осталось ходов: {TURNS}', font=('Verdana', 14))
turns_label.place(relx=0.07, rely=0.5)

btn_guess = tk.Button(window, text='OK', width=15, command=guess)
btn_guess.place(relx=0.07, rely=0.7)
btn_cancel = tk.Button(window, text='Cancel', width=15, command=cancel)
btn_cancel.place(relx=0.55, rely=0.7)

used_letters_label = tk.Label(window, text='Log:')
used_letters_label.place(relx=0.5, rely=0.9, anchor='center')

# label_text = tk.Label(window, text='Hello, ITMO!', font=('Verdana', 20), 
#                       bg='red', fg='white')
# label_text.pack()

# user_entry = tk.Entry(window, width=10)
# user_entry.pack()

# button1 = tk.Button(window, text='OK', command=test)
# button1.pack()

window.mainloop()