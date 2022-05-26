"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
from hashlib import pbkdf2_hmac
from binascii import hexlify


def hash_creator(password, salt):
	return hexlify(pbkdf2_hmac(hash_name='sha256',
	password=bytes(password, encoding='utf-8'),
	salt=salt,
	iterations=1)) 


### это будет в базе
salt = b'my_salt'

password = input('Введите пароль: ')

hash_pass = hash_creator(password, salt)

# hash_obj = pbkdf2_hmac(hash_name='sha256',
# 	password=b'{password}',
# 	salt=salt,
# 	iterations=1)

# result = hexlify(hash_obj)
####

print(f'В базе данных хранится строка: {hash_pass}')


passwd = input('Введите пароль еще раз для проверки: ')

if hash_creator(passwd, salt) == hash_pass:
	print('Вы ввели правильный пароль')
else:
	print('Вы ввели неверный пароль')

