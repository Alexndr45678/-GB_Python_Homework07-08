from view import read_data
from datetime import datetime


def result_log(dct: dict):
    time = datetime.now().strftime('%H:%M:%S')
    with open('log.csv', 'a') as file:
        file.write('{}{}'
                   .format(time, dct['result']))
