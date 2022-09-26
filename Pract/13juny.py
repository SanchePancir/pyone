


import os

list_paths = []
# Генерируем список всей файлов в Е диске и записываем его в файл text.txt
for adress, papka, file in os.walk('E:\\'):
	for i in file:
		full_path = os.path.join(adress, i)
		list_paths.append(full_path)

# 'r' - открыть для чтения (по умолчанию)
# 't' - открыть в текстовом режиме (по умолчанию)
# 'w' - открыть для записи, содержимое файла удаляется, если файла нет, то созд.новый
# 'a' - открыть для дозаписи в конце файла, если файла нет, то созд.новый
# 'b' - открытие в бинарном режиме (прочитать с бинарным режимом 'rb')
# '+' - открыть для чтения и записи 'r+', 'w+', 'a+'





r = open('text.txt', 'w')
for x in list_paths:
	r.write(x + '\n')

r.close() # Закрыть файл 


# Все пути к файлам где есть часть указанного слова
r = open('text.txt')
for i in r:
	if 'juny.py' in i:
		print(i)

#Кодировка______________________________________________________________

r = open('text2.txt', 'w', encoding = 'utf-8') # стандартная кодировка - 1251
r.write('stroka текста')
print(r)

r.close()

h = open('text2.txt', encoding = 'utf-8') 
# В этом случае, без указания кодировки текст будет не читабелен
print(h.read())

# Работа с бинарным режимом:_____________________________________________
r = open('python-3.10.4-amd64.exe', 'rb')
y = open('Копия python-3.10.4-amd64.exe', 'wb')

while True:
	var = r.read(1024*1024) # or 1048576 мб в байте
	print(var.__sizeof__()) # сколько оперативной памяти занимает объект
	if var.__sizeof__() == 33:
		break
	y.write(var)

print('Контроль')
r.close()
y.close