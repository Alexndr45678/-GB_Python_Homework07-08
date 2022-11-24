# def read_data() -> dict:

print ("Приветствуем Вас в калькуляторе Python")

FirstNum = float (input("Введите первое число: "))
SecondNum = float (input("Введите второе число: "))

MathAction = input('''Выберите действие из приведенных ниже для выполнения действия:
+ для сложения
- Для вычитания
* Для умножения
/ Для деления
^ Для возведения в квадрат \n''')

def CheckOperator(MathAction):
    operator = False
    while not operator:
        try:
            operator = str(('MathAction'))
            if operator == '^' or '*' or '/' or '^' or '+' or '-':
                operator = True
        except ValueError:
            print('Нужно ввести корректный оператор\n')
    return abs(operator)

dct = {
    'num1': '',
    'num2': '',
    'operator': '',
    'result': '',
    'isComplex1': True,
    'isComplex2': True,
}
dct ['num1'] = FirstNum
dct ['num2'] = SecondNum
dct ['operator'] = MathAction
