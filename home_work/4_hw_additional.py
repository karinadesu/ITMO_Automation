class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def start(self):
        return 'Автомобиль заведен'

    def turn_off(self):
        return 'Автомобиль заглушен'

    def year(self):
        return 'Тип автомобиля - {}'.format(self.year())

    def color(self):
        return 'Цвет автомобиля - {}'.format(self.color())




