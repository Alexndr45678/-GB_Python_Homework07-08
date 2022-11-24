import view

def calculate():
    if MathAction == '+':
        print('{} + {} = '.format(FirstNum, SecondNum))
        print(FirstNum + SecondNum)
    elif MathAction == '-':
        print('{} - {} = '.format(FirstNum, SecondNum))
        print(FirstNum - SecondNum)
    elif MathAction == '*':
        print('{} * {} = '.format(FirstNum, SecondNum))
        print(FirstNum * SecondNum)
    elif MathAction == '/':
        print('{} / {} = '.format(FirstNum, SecondNum))
        print(FirstNum / SecondNum)
    # else:
    #     print('Некорректный оператор. Перезапустите программу.')
        
