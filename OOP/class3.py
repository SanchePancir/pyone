# Полиморфизм - если есть метод а не надо думать что делает тоже самое в другом классе

class A: # Супер классы - они ни от кого не наследуются
    def a(self):
        print('A')

class B: # Супер классы - они ни от кого не наследуются
    def a(self):
        print('B')

class C(B): # Подкласс класса B
    def a(self):
        print('C')

class D(C, A): # Наследуется от класса С и В и А
    def a(self):
        super().a() # Также от какого класса начинать поиск: super(B, self).a()
        print(self.__class__.__mro__)

D().a()


class Verification:
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError ('Слабый пароль')
    
    def save(self):
        with open('user', 'a') as r:
            r.write(f'{self.login, self.password}'+'\n')