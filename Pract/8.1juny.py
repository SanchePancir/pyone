import os
import time

spisok = []

for adress, dirs, files in os.walk('C:\\Users\snovs\Desktop\адинадин'):
# walk - функция генератор, при каждом обращении будет выдавать перечисление значений
	spisok.append(adress) # Добавляем значения
	for file in files:
		full = os.path.join(adress, file)
		if '.MOV' in full:
			spisok.append(full)
		if time.time() - os.path.getctime(full) < 86400: # Столько сек в сутках
			spisok.append(full)

print(spisok)

# Все файлы не являющиеся jpg
spisok1 = []

for adress, dirs, files in os.walk('C:\\Users\snovs\Desktop\рутс'):
	spisok1.append(adress)
	for fale in files:
		full = os.path.join(adress, file)
		if not 'jpg' in full:
			spisok1.append(full)
print(spisok1)

