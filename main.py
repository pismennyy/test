
import sys


def a_input():
    a = []
    try:
        for i in range(int(input("Сколько объектов должно быть в А?  "))):
            a.append(input(f'Введите {i+1} объект: '))
        return a
    except ValueError:
        print('Введите число')
    return None


def b_input():
    b = []
    try:
        for i in range(int(input("Сколько объектов должно быть в B"))):
            b.append(input(f'Введите {i+1} символов: '))
        return b
    except ValueError:
        print('Введите число')
    return None



def zada4a_1 (a,b):
    temp = []
    for i in a:
        if a.count(i) == 1 and i not in b:
            temp.append(i)
    for i in b:
        if b.count(i) == 1 and i not in a:
            temp.append(i)
    print(temp)


def zada4a_2 (a,b):
    temp = []
    for i in set(a):
        if a.count(i) != 1 and i not in b:
            temp.append(i)
        print(temp)


def zada4a_3 (a,b):
    temp = []
    for i in set(a):
        if a.count(i) != 1 and i not in b:
            temp.append(i)
    for i in set(b):
        if b.count(i) != 1 and i not in a:
            temp.append(i)
        print(temp)


def a_b_print(a,b):
    print(a,b)


def main():
    '''
    Менюшка
    '''
    a = None
    b = None
    while True:
        com = input('''
        Команды:
        1 - Ввести A
        2 - Ввести B
        3 - Задание 1
        4 - Задание 2
        5 - Задание 3
        6 - Вывести A и B
        0 - Выход из программы
        ''')
        if com =='0':
            sys.exit()
        elif com == '1':
            a = a_input()
        elif com == '2':
            b = b_input()
        elif com =='3' and a is not None and b is not None:
            zada4a_1(a,b)
        elif com =='4' and a is not None and b is not None:
            zada4a_2(a,b)
        elif com == '5' and a is not None and b is not None:
            zada4a_3(a, b)
        elif com == '6':
            a_b_print(a,b)
        else:
            print('Неправильно введено значение')


if __name__ == '__main__':
    main()
