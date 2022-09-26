
# Открываем файлы с пк и исключаем ошибки

import sys

url_list = [
'C:\\Users\\snovs\\Desktop\\text.txt', 
'C:\\Users\\snovs\\Desktop\\text2.txt',
'C:\\Users\\snovs\\Desktop\\text25.txt',
'C:\\Users\\snovs\\Desktop\\text3.txt'
]

list_defect = []
list_info = []
try:
	for url in url_list:
		try:
			r = open(url)
			list_info.append(r.read()) #Добавляем информацию через мет.append
			print('Файлы присутствуют')

		except Exception:
			list_defect.append(url) 
			print('Нет файла')
			sys.exit() # Обрывает программа, генерация ошибки
			continue
finally:
	r = open('C:\\Users\\snovs\\Desktop\\save.txt', 'a')
	for i in list_info:
		r.write(i)
	r.write(str(list_defect))
	r.close()	
	print('Я все записал, не смотря ни на что!')






print(list_defect) # Показывает какого файла нет
print(list_info) # Показывает какой текст написан в имеющихся файлах
