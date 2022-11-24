from view import read_data
from datetime import datetime


def result_log(dct: dict):
    time = datetime.now().strftime('%H:%M:%S')
    with open('log.log', 'a') as file:
        file.write('{} => {} {} {} = {}\n'
                   .format(time, dct['num1'], dct['operator'], dct['num2'], dct['result']))


dct = {
    'num1': '2',
    'num2': '3',
    'operator': '+',
    'result': '5',
}

result_log(dct)
