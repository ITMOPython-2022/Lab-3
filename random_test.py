import random


code = ''
letters_list = 'abcdefghijklmnopqrstuvwxyz'
for i in range(3):
    code += random.choice(letters_list)

print(code)

print(random.randint(0, 10))