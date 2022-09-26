#  В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива.

from collections import Counter



def checkio(numbers):
    counter = Counter(numbers)
    return [n for n in numbers if counter[n] > 1]


print(checkio([1, 2, 3, 1, 3])) # == [1, 3, 1, 3]
print(checkio([1, 2, 3, 4, 5])) # == []
print(checkio([5, 5, 5, 5, 5])) # == [5, 5, 5, 5, 5]



print('  ')
#__________________________________________________________________________


# print('Пароль принят' if input() == input() else 'Пароль не принят')

#num = str(input())
#print('ДА' if int(num[0]) + int(num[-1]) == int(num[1]) - int(num[2])  else 'НЕТ')



#nums = (int(input()) for i in range(5))
#a, b = min(nums), max(nums)
#print(f"Наименьшее число = {a}", f"Наибольшее число = {b}", sep="\n")

########### print(sum(abs(float(input())) for _ in range(5))) ##################

#p1, p2, q1, q2 = [int(input()) for i in range(4)]
#print(abs(p1 - q1) + abs(p2 - q2))

# print(max(c1, c2, c3, key=len))

#if len(s) == 1 and s in 'aeiou':
    #print('YES')


# ФИБОНАЧЧИ
      
n = 1
num1 = num2 = 1
print(num1, num2, end=' ')
for i in range(2, n):
    num1, num2 = num2, num1 + num2
    print(num2, end=' ')


print('\n')

#num = int(input())
#for i in range(num + 1):
    #print(str(i) * i)
#num = int(input())
#for i in range(num + 1):
    #print('*' * i)
    #if i > num / 2:
        #while i > 0:
            #i -= 1
            #print('*' * i)
        #break

#text = [input() for _ in range(int(input()))]

from random import randint
import sys
 
def get_sphere_answ(moodtype=0, rand_answ=1):
    if moodtype == 2:
        definit_positive = {1: 'Бесспорно', 2: 'Предрешено', 3: 'Никаких сомнений',
                            4: 'Определённо да', 5: 'Можешь быть уверен в этом'}
        return definit_positive[rand_answ]
    elif moodtype == 1:
        doubt_positive = {1: 'Мне кажется — «да»', 2: 'Вероятнее всего', 3: 'Хорошие перспективы',
                             4: 'Знаки говорят — «да»', 5: 'Скорее всего - «да»'}
        return doubt_positive[rand_answ]
    elif moodtype == 0:
        neutral = {1: 'Пока не ясно, попробуй снова', 2: 'Спроси позже', 3: 'Лучше не рассказывать',
                   4: 'Сейчас нельзя предсказать', 5: 'Сконцентрируйся и спроси опять'}
        return neutral[rand_answ]
    elif moodtype == -1:
        negative = {1: 'Даже не думай', 2: 'Мой ответ — «нет»', 3: 'По моим данным — «нет»',
                    4: 'Перспективы не очень хорошие', 5: 'Весьма сомнительно'}
        return negative[rand_answ]
 
def get_rand_mood():
    mood = randint(-1, 1 + 1)
    num_rand_answ = randint(1, 4 + 1)
    return mood, num_rand_answ
 
def get_user_quest():
    while True:
        user_quest = input('Каков ваш вопрос?\n>>> ')
        if user_quest == '':
            print('Шар молчит в ответ')
            continue
        elif user_quest.casefold() == 'выход':
            return 0
        else:
            break
    return
 
def main():
    print("Магический шар 8 - шуточный способ предсказывать будущее!")
    while True:
        user_action = get_user_quest()
        if user_action == 0:
            print('Всего доброго')
            sys.exit()
        else:
            mood, answ = get_rand_mood()
            print(get_sphere_answ(mood, answ))
            print('Для выхода наберите «выход»')
        continue
 
if __name__ == '__main__':
    main()



m, n, matrix = int(input()), int(input()), []
for i in range(m):
    matrix.append([input() for _ in range(n)])
    print(*matrix[i])

