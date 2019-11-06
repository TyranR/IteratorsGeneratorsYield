# Написать генератор, который принимает путь к файлу.
# При каждой итерации возвращает md5 хеш каждой строки файла.

import hashlib
from pprint import pprint


def md5_func(mystring):
    """
    Принимает строку, возвращает её md5 хэш
    """
    print
    return hashlib.md5(mystring.encode('utf-8')).hexdigest()


def string_input():
    """
    Получаем файл или путь к файлу
    """
    # user_path = input("Введите путь к файлу: ")
    user_path = 'result.txt'
    return user_path


def generator(file):
    """
    Итерируемся по каждой строке
    """
    for row in file:
        yield row


def main():
    user_path = string_input()
    my_file = open(user_path, mode='r', encoding='utf-8')
    my_generator = generator(my_file)
    for line in my_generator:
        print(f"{line} = md5 {md5_func(line)}")
    my_file.close()


main()