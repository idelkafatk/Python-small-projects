import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
symbols = 'il1Lo0O'
chars = ''


def generate_passwords():
    global chars
    count = int(input('Введите количество паролей для генерации'))
    x = int(input('Введите длину пароля'))
    numbers = input('Включать ли цифры? "да" или "нет"')
    if numbers == "да":
        chars += digits
    up= input('Включать ли заглавные буквы? "да" или "нет"')
    if up == "да":
        chars += uppercase_letters
    low = input('Включать ли строчные буквы? "да" или "нет"')
    if low == "да":
        chars += lowercase_letters
    sym = input('Включать ли символы? "да" или "нет"')
    if sym == "да":
        chars += punctuation
    sym2 = input('Включать ли символы il1Lo0O? "да" или "нет"')
    if sym2 == "да":
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')

    for i in range(1, count + 1):
        print(i,'.', *random.sample(chars, x), sep='')
    return 'Спасибо за использование программы!'


print(generate_passwords())