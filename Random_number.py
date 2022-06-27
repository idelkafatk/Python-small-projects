import random

again = 'OK'


def is_valid(x):
    if x.isdigit() and 1 <= int(x) <= 100:
        while number != x:
            x = int(x)
            if number < x:
                x = int(input('Слишком много, попробуйте еще раз'))
            elif number > x:
                x = int(input('Слишком мало, попробуйте еще раз'))
        print('Вы угадали, поздравляем!')
    else:
        x = input('А может быть все-таки введем целое число от 1 до 100?')
    global again
    again = input('Введите "OK", если хотите сыграть еще...')
    if again == 'OK':
        return 'Поехали дальше...'
    else:
        return 'Cпасибо за игру!!'


while again == 'OK':
    number = random.randint(1, 100)
    num = input('Введите целое число от 1 до 100...')
    print(is_valid(num))


