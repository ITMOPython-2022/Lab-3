import tkinter as tk
from word_select import choose_word
from tkinter import messagebox
from string import ascii_uppercase


def step_increase():
    global STEP
    STEP += 1
    return STEP


def guess():
    word = word_entry.get()
    if len(word) != 5 or word.isalpha() is False:
        return 0
    word = word.upper()
    word_entry.delete(0, 'end')

    result = word_check(word)
    step_increase()
    if result == 5:
        messagebox.showinfo('Победа!', 'Вы угадали слово!')
        window.destroy()
    elif STEP == 6 and result != 5:
        messagebox.showerror('Не победа(', f'Вы не угадали слово {WORD_TO_GUESS}')
        window.destroy()


def word_check(word_to_check):
    global USED_LETTERS
    count = 0
    for i, letter in enumerate(word_to_check):
        if letter == WORD_TO_GUESS[i]:
            letters[i + STEP * 5].configure(text=letter,
                                            bg='green',
                                            fg='white')
            if tracker.get() == 1 and STEP < 5:
                letters[i + STEP * 5 + 5].configure(text=letter,
                                                    fg='grey')
            count += 1
        elif letter != WORD_TO_GUESS[i] and letter in WORD_TO_GUESS:
            letters[i + STEP * 5].configure(text=letter,
                                            bg='yellow')
        else:
            letters[i + STEP * 5].configure(text=letter)
            USED_LETTERS = USED_LETTERS.replace(letter, ' ')
    
    used_label.configure(text=USED_LETTERS)
    return count


window = tk.Tk()
window.title('My app')
window.geometry('270x720')
window.resizable(0, 0)
bg_img = tk.PhotoImage(file='image2.png')

STEP = 0
WORD_TO_GUESS = choose_word()
USED_LETTERS = ' '.join(ascii_uppercase).replace('M N', 'M\nN')

cols = 5
rows = 6
letters = []

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

for i in range(rows):
    for j in range(cols):
        letter_label = tk.Label(window,
                                text=' ',
                                font=('Consolas', '50'),
                                bg='white')
        letter_label.grid(row=i, column=j, padx=5, pady=5)
        letters.append(letter_label)

tracker = tk.IntVar()
checkbox = tk.Checkbutton(window,
                          text='Track next letters',
                          variable=tracker)
checkbox.grid(row=i+1, column=0, columnspan=5)

word_entry = tk.Entry(window, width=7, font=('Verdana 24'))
word_entry.insert(0, 'blank')
word_entry.grid(row=i+2, column=0, columnspan=3, pady=10)

btn = tk.Button(window, 
                text='Guess', 
                width=6,
                font=('Verdana 16'),
                command=guess)
btn.grid(row=i+2, column=3, columnspan=2)

used_label = tk.Label(text=USED_LETTERS,
                      font=('Consolas 14'),)
used_label.grid(row=i+3, column=0, columnspan=5, pady=5)

window.mainloop()