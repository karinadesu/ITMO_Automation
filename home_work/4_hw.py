class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return 'Площадь =', self.length * self.width

    def perimeter(self):
        return 'Периметр =', (self.length + self.width) * 2


rectangle1 = Rectangle(3, 6)
rectangle2 = Rectangle(10, 21)
rectangle3 = Rectangle(11, 12)
print('Длина =', rectangle1.length, 'Ширина =', rectangle1.width, rectangle1.area(), rectangle1.perimeter())
print('Длина =', rectangle2.length, 'Ширина =', rectangle2.width, rectangle2.area(), rectangle2.perimeter())
print('Длина =', rectangle3.length, 'Ширина =', rectangle3.width, rectangle3.area(), rectangle3.perimeter())


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a, '+', self.b, '=', self.a + self.b

    def multiplication(self):
        return self.a, '*', self.b, '=', self.a * self.b

    def division(self):
        return self.a, '/', self.b, '=', self.a / self.b

    def subtraction(self):
        return self.a, '-', self.b, '=', self.a - self.b


nums = Math(3, 4)
print(nums.addition())
print(nums.multiplication())
print(nums.division())
print(nums.subtraction())


class Button:

    type: str = 'Кнопка'

    def __init__(self, text, loc=''):
        self.text = text
        self.loc = loc

    def click(self):
        return 'Клик по кнопке - {}'.format(self.text)


btn1 = Button('Text Box')
btn2 = Button('Check Box')
btn3 = Button('Radio Button')
btn4 = Button('Web Tables')
btn5 = Button('Buttons')
btn6 = Button('Links')
btn7 = Button('Broken Links - Images')
btn8 = Button('Upload and Download')
btn9 = Button('Dynamic Properties')
print(btn1.click())
print(btn2.click())
print(btn3.click())
print(btn4.click())
print(btn5.click())
print(btn6.click())
print(btn7.click())
print(btn8.click())
print(btn9.click())


