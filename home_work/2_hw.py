def task_1() -> type:
    a: int = 5
    b: float = 5.6
    c: str = "IT's MOre than University"
    d: list = ['sushi', 'tako']
    e: bool = False

    for val in a, b, c, d, e:
        print(f'Тип {val} -', type(val))
    return type


task_1()


def task_2() -> list:
    # числа Фибоначчи
    a = [1, 2, 3, 5, 8, 13, 21]

    print('\nTask 2', a[:3])
    return a


task_2()


def task_3(x: int) -> int:
    square = x ** 2
    return square


print('\nTask 3', (task_3(11)))
