
# Декораторы
# - это функция, которая позволяет обернуть другую функцию в свой код(для модификации)

# Обработчик ошибок:

def decor(f):
	def wrapper():
		try:
			h = f()
		except Exception:
			print('Повторите ввод... ')
			h = f()
		return h
	return wrapper

@decor # maker = decor(make)
def make():
	enter = float(input('Введите число: '))
	return enter

@decor
def make2():
	enter = float(input('Введите число опять: '))
	return enter

make2()
make()

