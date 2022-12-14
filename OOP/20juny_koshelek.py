# ООП 1

# Объект - это любая единица информации в патями
# Экземпляр - конкретный объект какого-то класса
# Класс - инструкция по созданию объектов определенного типа
# Метод - функция в классе для воздействия на объект
# Инкапсуляция - добавление "__" вначале объекта, чтобы его нельзя было изменить
# Композиция - когда вызываем внутри класса другой класс


class Purse:
    
    def __init__(self, valuta, name='Unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Не достаточно средств')
            raise ValueError ('Не достаточно средств')
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        return print(self.__money)

    def __del__(self):
        print ('Кошелек удален')


x = Purse('USD')
y = Purse('EUR', 'Bill')
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()
