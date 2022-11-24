def read_data() -> dict:
    dct = {
    'FirstNum': '',
    'SecondNum': '',
    'operator': '',
    'final': '',
    'isComplex1': True,
    'isComplex2': True,
}
    dct ['FirstNum'] = FirstNum
    dct ['SecondNum'] = SecondNum
    dct ['operator'] = MathAction

print ("Приветствуем Вас в калькуляторе Python")

FirstNum = float (input("Введите первое число: "))
SecondNum = float (input("Введите второе число: "))

MathAction = input('''Выберите действие из приведенных ниже для выполнения действия:
+ для сложения
- Для вычитания
* Для умножения
/ Для деления
^ Для возведения в квадрат \n''')

def operator():
    if operator == '+' or '-' or '/' or '^' or '*':
        operator = MathAction
        return True
    else:
        print('Нужно ввести корректный оператор\n')
        return operator()



dct = {
    'num1': '2',
    'num2': '3',
    'operator': '+',
    'result': '5',
    'isComplex1': True,
    'isComplex2': True,
}
dct ['FirstNum'] = FirstNum
dct ['SecondNum'] = SecondNum
dct ['operator'] = MathAction

# def again():
#     calc_again = input(
#         'Хотите продолжить работу? Введите Y для продолжения или N для завершения.')
#     if calc_again.upper() == 'Y':
#         calculate()
#     elif calc_again.upper() == 'N':
#         print('До свидания.')
#     else:
#         again()
#         calculate()

def print_data(a: dict):
    pass


#     is_num = False
#     while not is_num:
#         try:
#             num = float(input('Введите число: '))
#             if num:
#                 is_num = True
#         except ValueError:
#             print('Нужно ввести число\n')
#     return abs(num)
