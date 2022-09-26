
## Менеджер контекста with as (нужен, чтобы при ошибке все сохранилось)

r = open('C:\\Users\\snovs\\Desktop\\text.txt', 'a')
r.write('\nТест')
r.close()

print('Все нормально')

#_______________________________________________

with open('C:\\Users\\snovs\\Desktop\\text.txt', 'a') as r:
	r.write('\nПервая надпись\n')
	10/0 # ошибка появится, но изза with файл будет закрыт и сохранены данные
	r.write('Вторая надпись\n')
	# close не пишем, потому что файл после with закрывается автоматически

print('Снова все нормально')

#________________________________________________
#### Также можно обработать сохранение файла так:

r = open('C:\\Users\\snovs\\Desktop\\text.txt', 'a')
try:
	r.write('\nSomething\n')
	10/0
	r.write('Еще что-то написали')
finally:
	r.close()