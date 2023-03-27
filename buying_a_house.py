class House:

    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, discount: int) -> int:
        return round(self._price * (1 - discount / 100))

    def __repr__(self):
        return f'House area {self._area}, House price: {self._price}'


class SmallHouse(House):
    def __init__(self, _price):
        super().__init__(40, _price)

class Human:

    default_name: str = "Максим"
    default_age: int = 15

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house: House = None

    def money_account(self):
        while self.__money <= 0:
            try:
                money = float(input("Введите ваш счёт: "))
                if money < 0:
                    print("Не должен быть отрицательным")
                    continue
                elif money == 0:
                    print("Хочется больше денег")
                    continue
                self.__money = money
            except ValueError:
                print('Введено не число')

    @property
    def house_money(self):
        return self.__house, self.__money

    def info_human(self):
        print(f"""Name: {self.name} Age: {self.age} Money: {self.__money} House: {self.__house}""")

    def default_info(self):
        print(f'Имя: {self.default_name}''\n'f'Возраст: {self.default_age}')

    def __make_deal(self, house, price_house):
        self.__house = house
        self.__money -= price_house
        if self.__money > self.price_house:
            print(f'Поздравляю вы купили дом, на вашем счету: {self.__money}')
        else:
            print('У вас не достаточно средств')

    def deal(self, house: House, money):
        _price: float = house._price()
        money: float = money
        self.__make_deal(house, _price, money)

    def earn_money(self, amount: float):
        self.__money += amount
        return (f"Кредит на {amount} оформлен. Сейчас у вас: {self.__money}")

    def buy_house(self, house: House, discount: int) -> None:
        if house.final_price(discount) <= self.__money:
            self.deal(house, house.final_price(discount))
        else:
            print('Недостаточно денег')

if __name__ == '__main__':
    g = Human()
    g.money_account()
    g.default_info()
    g.info_human()
    house = SmallHouse(10000)
    g.buy_house(house, 10)
    g.earn_money(2000)
    g.info_human()
    g.buy_house(house, 10)
    g.earn_money(5000)
    g.info_human()
    g.buy_house(house, 10)


