try:
    x = int(input("Введите делимое: "))
    y = int(input("Введите делитель: "))
    результат = x / y
    print("Результат:", результат)
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно.")
except ValueError:
    print("Ошибка: Введено нечисловое значение.")