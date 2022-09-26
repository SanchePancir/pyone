
class Wallet:

    def __init__(self, valuta):
        if valuta not in ('RUB'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta

    def top_up_balance(self, howmany):
        self.__money += howmany
        return print('Баланс пополнен на:', howmany, 'рублей!')
    
    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Недостаточно средств!')
            raise ValueError
        self.__money -= howmany
        return print('С баланса списано:', howmany, 'рублей!')

    def info(self):
        return print('Ваш текущий баланс:', self.__money, 'рублей!')



x = Wallet('RUB')
x.top_up_balance(1000)
x.top_down_balance(328)
x.info()
