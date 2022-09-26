# Удалить cписок до символа
#remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
#remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]

from cgitb import reset
from unittest import result


def remove_all_before(items: list, border: int):
    if border in items:
        for i in range(len(items)):
            if items[i] == border: # <- нашли border
                return items[i:] # <- вернули всё, что после
    else:
        return items


print(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) 
print(remove_all_before([1, 1, 5, 6, 7], 2)) 
print(remove_all_before([], 0)) 

# Не мое решение:
def remove_all_before_1(items: list, border: int):
    return items[items.index(border):] if border in items else items







print('')
#__________________________________________________________________
# Проверить все ли символы являются заглавными.

#def is_all_upper(text):
    #if text == text.upper() or text == '' or text == int:
        #return True
    #else:
        #return False
    
def is_all_upper(text):
    return text.upper() == text # text.isupper()


print(is_all_upper('ALL UPPER')) #== True
print(is_all_upper('all lower')) #== False
print(is_all_upper('mixed UPPER and lower')) #== False
print(is_all_upper('')) #== True
print(is_all_upper('444')) #== True
print(is_all_upper('55 55 5')) #== True







print('')
#__________________________________________________________________
# В данном списке первый элемент должен стать последним.

def replace_first(numbers):
    if len(numbers) > 1:
        numbers.append(numbers[0])
        numbers.pop(0)
        return numbers

    else:
        return numbers

##############################    
def replace_first(items):
    if items:
        items.append(items.pop(0))
    return items
################################

print(replace_first([0, 5, 2, 3, 4])) 
print(replace_first([10, 10])) 







print('')
#__________________________________________________________________
# У вас есть число и нужно определить какая цифра из этого числа является наибольшей.

def max_digit(num):
    return int(max(list(str(num))))

###############################
def max_digit(number: int) -> int:
    return max(map(int, str(number)))
###############################

print(max_digit(0)) # == 0
print(max_digit(52)) # == 5
print(max_digit(634)) # == 6
print(max_digit(1)) # == 1
print(max_digit(10000)) # == 1







print('')
#__________________________________________________________________
# Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.

def beginning_zeros(num):
    result = 0
    for i in str(num):
        if i == '0':
            result += 1
        else:
            break
    return result
   
####################################
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))
#####################################            

print(beginning_zeros('100')) # == 0
print(beginning_zeros('001')) # == 2
print(beginning_zeros('001001')) # == 2
print(beginning_zeros('012345679')) # == 1
print(beginning_zeros('0000')) # == 4






print('')
#__________________________________________________________________
# Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст внутри

def between_markers(text, begin, end):
    begin_index = text.find(begin) + len(begin)
    end_index = text.find(end)
    if begin not in text:
        begin_index = 0
    if end not in text:
        end_index = len(text)
    return text[begin_index:end_index]


################################################
def between_markers(text, begin, end):
    return text[text.index(begin)+1:text.index(end)]
###############################################

print(between_markers('What is >apple<', '>', '<')) #== 'apple'







print('')
#__________________________________________________________________
# Разделите строку на пары из двух символов.
# Если строка содержит нечетное количество символов, в конце ('_').
def split_pairs(text):
    n = 2
    new_list = []
    for i in range(0, len(text), n):
        element = text[i: i + n]
        if len(element) == 1:
            new_list.append(element + '_')
        else:
            new_list.append(element)
    return new_list

#########################################
def split_pairs(a):
    return [ch1 + ch2 for ch1, ch2 in zip(a[::2],a[1::2]+'_')]
#########################################


print(split_pairs('abcd')) #== ['ab', 'cd']
print(split_pairs('abc')) #== ['ab', 'c_']





print('')
#__________________________________________________________________
# На вход Вашей функции будет передано одно предложение, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.

def correct_sentence (text):
    new_text = text[0].upper() + text[1:] #capitalize()
    if text[-1] == '.':
        return new_text
    else:
        return new_text + '.'

##############################################################
def correct_sentence(text):  
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")
##############################################################


print(correct_sentence("Greetings, FRIEnds")) # == "Greetings, FRIEnds."
print(correct_sentence("greetings, friends")) # == "Greetings, friends."
print(correct_sentence("Greetings, friends.")) # == "Greetings, friends."






print('')
#__________________________________________________________________
# Проверить является ли число четным или нет. 

def is_even(num):
    return num % 2 == 0

###########################################
def is_even(num):
    return num & 1 == 0
###########################################

print(is_even(2)) # == True
print(is_even(5)) # == False
print(is_even(0)) # == True






print('')
#__________________________________________________________________
# Найдите ближайшее значение к переданному.


def nearest_value (run, num):
    run = list(run) 
    run.sort()
    result = [abs(i - num) for i in run]
    return run[result.index(min(result))]

print(nearest_value({4, 7, 10, 11, 12, 17}, 9)) # == 10
print(nearest_value({-7, -6, 4, 5, 12, 17}, -4)) # == -6





print('')
#__________________________________________________________________
