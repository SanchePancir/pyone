from jinja2 import Template

name = 'Саша'
age = 28

tm = Template('Привет, мне {{a}} лет, меня зовут {{n.upper()}}!')
msg = tm.render(n = name, a = age) # Используется как словарь

print(msg)

# Или как класс:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    def getAge(self):
        return self.age


per = Person('Саша', 29)
tm = Template('Привет, мне {{p.age}} лет, меня зовут {{p.name}}?')
msg = tm.render(p = per)

print(msg)

# Или:
tm = Template('Привет, мне {{p.getAge()}} лет, меня зовут {{p.getName()}}.')
msg = tm.render(p = per)
print(msg)

# Или через словарь:

per = {'name': 'Федор', 'age': 34}

tm = Template('Привет, мне {{p.age}} лет, меня зовут {{p.name}}!!!')
msg = tm.render(p = per)
print(msg)
print("")
#########################################################################
# Экранирование:

data = '''{% raw %}Модуль Jinja вместо
определения {{name}}
подставляет соответствующее значение{% endraw %}'''

tm = Template(data)
msg = tm.render(name='Сашка')

print(msg)
print('')

link = '''В HTML-документе ссылки определяютс так:
<a href="#">Ссылка</a>'''

tm = Template('{{link | e}}')
msg = tm.render(link = link)

print(msg)
print("")
#############################################################################

from markupsafe import escape

link = '''В HTML-документе ссылки определяютс так:
<a href="#">Ссылка</a>'''

msg = escape(link)
print(msg)
print("")
#############################################################################

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{%elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities = cities)

print(msg)
print("")
#############################################################################