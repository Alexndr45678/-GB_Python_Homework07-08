def read_data(dct) -> dict:
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

def print_data(dct):
    print(f"{dct['num1']} {dct['operator']} {dct['num2']} = {dct['result']}")
    repeat = input(
        'Хотите продолжить работу? Введите Y для продолжения или N для завершения.')
    if repeat.upper() == 'Y':
        read_data()
        # calculate()
    elif repeat.upper() == 'N':
        print('До свидания.')
        exit()