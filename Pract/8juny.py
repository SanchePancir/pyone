import os
import time

x = 0
while x < 5:
	x += 1
	print(x)
	time.sleep(1)
print('Загрузка окончена!\n')






# Метод system. Доступ через указания метода "os.", далее () - аргумент,
# - данные для обработки
while True:
	sayt = input('Введите адрес сайта:\n')
	
	if sayt == 'Завершить':
		break

	if 'https://' in sayt: # Оператор in проверяет есть ли в записли 'https://'
		os.system('start ' + sayt) # Команда открывает сайт
		print('if')

	elif 'www.' in sayt:
		sayt = 'https://' + sayt
		os.system('start ' + sayt)
		print('elif')

	else:
		sayt = 'https://www.' + sayt
		os.system('start ' + sayt)
		print('else')

time.sleep(5) # Следующее действие произойдет через 5 секунд
os.startfile('C:/Пользователи/snov/Рабочий стол/Комикс.txt') # откроется указанный файл
