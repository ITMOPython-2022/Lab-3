import random


def choose_word() -> str:
    try:
        with open('words_en.txt') as words_list:
            words = words_list.readlines()
            myword = random.choice(words)
            return myword[:5]
    except FileNotFoundError:
        print('Файл не найден!')
        return 'BLANK'


if __name__ == '__main__':
    print(choose_word())