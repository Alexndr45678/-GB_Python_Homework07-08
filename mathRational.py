from view import FirstNum, MathAction, SecondNum

# 1 вариант


def calculate(dct: dict) -> dict:
    if MathAction == '+':
        print('{} + {} = {}'.format(FirstNum, SecondNum))
    elif MathAction == '-':
        print('{} - {} = {}'.format(FirstNum, SecondNum))
    elif MathAction == '*':
        print('{} * {} = {}'.format(FirstNum, SecondNum))
    elif MathAction == '/':
        print('{} / {} = {}'.format(FirstNum, SecondNum))
    elif MathAction == '^':
        print('{} ** {} = {}'.format(FirstNum, SecondNum))
    # else:
    #     print('Некорректный оператор. Перезапустите программу.')


# 2 вариант
# def calculate(dct: dict)-> dict:
#     if MathAction == '+':
#         dct['result']('{} + {} = {}'.format(FirstNum, SecondNum))
#     elif MathAction == '-':
#         dct['result']('{} - {} = {}'.format(FirstNum, SecondNum))
#     elif MathAction == '*':
#         dct['result']('{} * {} = {}'.format(FirstNum, SecondNum))
#     elif MathAction == '/':
#         dct['result']('{} / {} = {}'.format(FirstNum, SecondNum))
#     elif MathAction == '^':
#         dct['result']('{} ** {} = {}'.format(FirstNum, SecondNum))
