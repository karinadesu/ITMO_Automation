def fun_1(a, b):
    if a > b:
        return a
    else:
        return b


print('max number:', fun_1(12411,124124124))


def fun_2(a, b):
    x = abs(a - b)
    if x == 135:
        return 'Yes'
    else:
        return 'No'


print('difference on 135:', fun_2(0,135))


def fun_3(month):
    if month in range(1, 3) or month == 12:
        print('Зима')
    elif month in range(3, 6):
        print('Весна')
    elif month in range(6, 9):
        print('Лето')
    elif month in range(9, 12):
        print('Осень')
    else:
        print('Введите число от 1 до 12')


fun_3(8)


def fun_4(x, y, z):
    values = [x, y, z]
    if all(v > 10 for v in values):
        print('yes')
    else:
        print('no')


fun_4(10,11,11)


array = [234, -222, 2, 0, -133332]


def fun_5(arr):
    i = 0
    for a in arr:
        if a > 0:
            i = i + 1

    return i


print('Количество положительных чисел:', fun_5(array))


def fun_6(years, months):
    days_in_month = 29
    months_in_year = 12
    days = years * months_in_year * days_in_month + months * days_in_month

    return days


print('Количество дней:', fun_6(1, 6))


