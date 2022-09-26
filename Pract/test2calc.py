# Калькулятор кала v2

from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

print(Back.GREEN)
print(Fore.BLACK)

what = input("Что нужно тебе, черт? (+, -) ")

print(Back.CYAN)

a = float(input("Напиши первое число, быстрей бля: "))
b = float (input("Введи второе число, ишак: "))

print(Back.YELLOW)

#Условия:

if what == "+":
    c = a + b
    print("Результат твоего говна: " + str(c))
elif what == "-":
    c = a - b
    print("Результат твоего говна: " + str(c))
else:
    print("Тупой, это не верная операция!")

input
