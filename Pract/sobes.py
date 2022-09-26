import string

# ГЕНЕРАТОР СПИСКА

#in range(1,21)
#slovar = {a: x for st in range (1,21)}

#g = {"a":11}
#print(type(g))
#bbb= string.ascii_lowercase[0:20]

#aaa = zip(bbb, range[1,21])
#print(aaa)

#dicts = {a: b for a, b in zip(string.ascii_lowercase, range[1,21])}
#print(dicts)

#dict1 = {a: x for a in range(1,21) for x in string.ascii_lowercase}
#print(dict1)

lst_1 = [x for x in range(1,21)]
lst_2 = list(string.ascii_lowercase)
dict_1 = dict(zip(lst_1, lst_2))
# dict1 = {letter: num for letter, num in enumerate(string.ascii_lowercase, start=1)}
print(dict_1)


def func(first, second, n):
    if n > len(first):
        dicts = {}
        for i in range(len(first)):
            dicts[first[i]] = second[i]
        return dicts
    # Если больше 20 - то прекращается
    
    dicts = {}
    for i in range(n):
        dicts[first[i]] = second[i]
    return dicts

print(func(lst_1, lst_2, 44))

# Еще можно сделать так:

def func_1(first, second, length):
    dicty = dict(zip(first[:length], second))
    return dicty

print(func_1(lst_1, lst_2, 15))