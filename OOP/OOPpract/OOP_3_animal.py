

# Animal - name
# eat() - '{name} in eating'

# Dog - доп. атрибут breed, bark() - 'Dog named {name} in barking'
# Cat - доп. атрибутов нет, meow() - '{name} says Meow'
# Frog - доп. атрибутов нет, eat() - переопред., чтобы 'Frog with {name} in eating'

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f'{self.name} in eating!')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f'Dog named: {self.name} in barking!')

class Cat(Animal):
    def meow(self):
        print(f'{self.name} says "Meow"!')

class Frog(Animal):
    def eat(self):
        print(f'Frog with {self.name} in eating!')


a1 = Animal('Кукарака')
a1.eat()
d1 = Dog('Бульба', 'Фронтендер')
d1.bark()
с1 = Cat('Coocky')
с1.meow()
f1 = Frog('BMX')
f1.eat()