from datetime import datetime


def result_log(dct: dict):
    time = datetime.now().strftime('%H:%M:%S')
    with open('calculator.log', 'a') as file:
        file.write('{} ==> {} {} {} = {}\n'
                   .format(time, dct['num1'], dct['operator'], dct['num2'], dct['result']))
