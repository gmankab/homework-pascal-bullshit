from inspect import cleandoc


def factorial(num):
    answer = 1
    for i in range(1, num + 1):
        answer *= i
    return answer


def numlen(num):
    return len(str(num))


def file_input():
    return int(open('num.txt', 'r').read())


print(
    cleandoc(
        f'''
        Задание 1:
            Факториал числа 100 равен {factorial(100)}
            В это число входит {numlen(factorial(100))} цифр

        Задание 2:
            Функция вывода числа называется "{factorial.__name__}()"

        Задание 3:
            Функция ввода чисел из файла называется "{file_input.__name__}()"
        '''
    )
)
