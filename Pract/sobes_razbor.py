
import string

lst1 = [x for x in range(1,31)]
lst2 = list(string.ascii_uppercase)


def func(key, value, n):
    dictir = dict(zip(key[:n], value))
    return print(dictir)

func(lst1, lst2, 5)


def text(value):
    result = ''
    i = 0
    while i < len(value):
        next = '' if (i + 1 >= len(value)) else (value[i + 1])
        result += next + value[i]
        i += 2
    return print(result)


text('Саша!')