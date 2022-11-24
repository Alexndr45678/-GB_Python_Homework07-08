def read_data() -> dict:
    print("Приветствуем Вас в калькуляторе Python")

    FirstNum = float(input("Введите первое число: "))
    SecondNum = float(input("Введите второе число: "))

    operator = False
    while not operator:
        try:
            MathAction = input('''Выберите действие из приведенных ниже для выполнения действия:
                + для сложения
                - Для вычитания
                * Для умножения
                / Для деления
                ^ Для возведения в квадрат \n''')
            if MathAction == '^' or '*' or '/' or '+' or '-':
                operator = True
            else:
                print('Нужно ввести корректный оператор\n')
        except ValueError:
            print('Нужно ввести корректный оператор\n')

    dct = {
        'num1': '',
        'num2': '',
        'operator': '',
        'result': '',
    }

    dct['num1'] = FirstNum
    dct['num2'] = SecondNum
    dct['operator'] = MathAction

    return dct
