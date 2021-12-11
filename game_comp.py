# шаг 1загадали случайное число
import random

number = random.randint(1, 100)
#print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('выберите уровень сложности: '))
max_count = levels[level]
print('у вас {} попыток'.format(max_count))

user_count = int(input('введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input('введите имя {} пользователя: '.format(i+1))
    users.append(user_name)
print(users)

is_winer = False
winer_name = None

while not is_winer:
    count += 1
    if count > max_count:
        print('все пользователи проиграли')
        break
    print('попытка № {}'.format(count))
    for user in users:
        print('ходит {}'.format(user))
        # шаг 2 пользователь вводит число
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winer = True
            winer_name = user
            break
        # шаг 3 сравнение результатов
        elif user_number < number:
            print('вы ввели слишком маленькое число')
        else:
            print('вы ввели слишком большое число')
else:
    print('победитель {]'.format(winer_name))
