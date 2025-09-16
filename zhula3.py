print("1) Сложение")
print("2) Вычитание")
print("3) Умножение")
print("4) Деление")
print("5) Целочисленное деление")
print("6) Остаток от деления")
print("7) Возведение в степень")
print("8) Поиск числа в списке")
print("9) Проверка тождественности")
print("10) Проверка нетождественности")
print("11) Побитовое И (&)")
print("12) Побитовое ИЛИ |")
print("13) Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ (^)")
print("14) Побитовое НЕ (~)")
print("15) Побитовый сдвиг влево (<<)")
print("16) Побитовый сдвиг вправо (>>)")
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    zhula = int(input('Введите цифру действия: '))
    if zhula in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16]:
        a = int(input('Введите первое число: '))
        if zhula != 14:
            c = int(input('Введите второе число: '))
    if zhula == 1:
        result = a + c
        print(result)
    elif zhula == 2:
        result = a - c
        print(result)
    elif zhula == 3:
        result = a * c
        print(result)
    elif zhula == 4:
        if c == 0:
            print('На 0 делить нельзя')
        else:
            result = a / c
            print(result)
    elif zhula == 5:
        if c == 0:
            print('На 0 делить нельзя')
        else:
            result = a // c
            print(result)
    elif zhula == 6:
        if c == 0:
            print('На 0 делить нельзя')
        else:
            result = a % c
            print(result)
    elif zhula == 7:
        result = a ** c
        print(result)
    elif zhula == 8:
        x = int(input('Введите элемент для проверки непринадлежности списку: '))
        if x in my_list:
            print("Этот элемент присутствует в списке")
        else:
            print("Этого элемента нет в списке")
    elif zhula == 9:
        if a == c:
            print("Объекты тождественны")
        else:
            print("Объекты не тождественны")
    elif zhula == 10:
        if a is not c:
            print("Объекты нетождественны")
        else:
            print("Объекты тождественны")
    elif zhula == 11:
        result = a & c
        print(result)
    elif zhula == 12:
        result = a | c
        print(result)
    elif zhula == 13:
        result = a ^ c
        print(result)
    elif zhula == 14:
        a = int(input('Введите число: '))
        result = ~a
        print(result)
    elif zhula == 15:
        if a >= 10000000:
            print('Число очень большое')
        else:
            result = a << c
            print(result)
    elif zhula == 16:
        if a >= 10000000:
            print('Число очень большое')
        else:
            result = a << c
            print(result)
except ValueError:
    print('Извините, произошла ошибка ввода, очень большие числа')