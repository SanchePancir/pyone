
class Person:
    def __init__(self, name, surname, place_of_birth, year_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth
 

    def person_info(self):
        print(f'Имя: {self.name},\nФамилия: {self.surname},\nМесто рождения: {self.place_of_birth},\nДата рождения: {self.year_of_birth},')
##  print(f'{self.name} тут учится!')
##  print(f'Этот ученик, по имени: {self.name} тут учится!')
    def get_age(self):
        birth = 2022 - self.year_of_birth
        birth = str(birth)
        if birth[-1] == '1' and birth[-2] != '1':
            text = 'год.'
        elif birth[-1] == '2' and birth[-2] != '1' or birth[-1] == '3' and birth[-2] != '1' or birth[-1] == '4' and birth[-2] != '1':
            text = 'года.'
        elif birth[-2] == '1':
            text = 'лет.'
        else:
            text = 'лет.'
        return print('Возраст:', birth, text +'\n')


p1 = Person('Александр', 'Снов', 'РФ', 1993)
p2 = Person('Мария', 'Маруськина', 'РФ', 2002)

#p1.person_info()
# можно еще вызвать: Person.person_info(p1)

p1.person_info()
p1.get_age()
p2.person_info()
p2.get_age()


######################____________________________________________________________
class Student(Person):
    def __init__(self, name, surname, place_of_birth, year_of_birth, ocenka):
        # Person.__init__(self, name, surname, place_of_birth, year_of_birth)
        super().__init__(name, surname, place_of_birth, year_of_birth)
        self.ocenka = ocenka
        print('Студент создан')
    
    def print_info(self):
        print(f'Этот ученик, по имени: {self.name} тут учится!')


s1 = Student('Александр', 'Снов', 'РФ', 1993, 4.5)