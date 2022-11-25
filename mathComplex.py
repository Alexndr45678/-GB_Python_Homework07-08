def calculate_complex(dct: dict):
    is_num1_complex = False
    is_num2_complex = False
    num1 = dct['num1']
    num2 = dct['num2']

    if dct['num1'][-1] == 'i':
        is_num1_complex = True
        num1 = dct['num1'][:-1]

    if dct['num2'][-1] == 'i':
        is_num2_complex = True
        num2 = dct['num2'][:-1]

    if dct['operator'] == '+':
        dct['result'] = sum_complex(
            is_num1_complex, is_num2_complex, num1, num2)
    elif dct['operator'] == '-':
        dct['result'] = sub_complex(
            is_num1_complex, is_num2_complex, num1, num2)
    elif dct['operator'] == '*':
        dct['result'] = mult_complex(
            is_num1_complex, is_num2_complex, num1, num2)
    elif dct['operator'] == '/':
        dct['result'] = div_complex(
            is_num1_complex, is_num2_complex, num1, num2)
    return dct


def sum_complex(is_num1_complex: bool, is_num2_complex: bool, num1: str, num2: str) -> str:
    result = ''
    if is_num1_complex and is_num2_complex:
        number = float(num1) + float(num2)
        if number % 1 == 0:
            result = str(int(number)) + 'i'
        else:
            result = str(number) + 'i'
    elif is_num1_complex:
        number = float(num1)
        if number % 1 == 0:
            num1 = str(int(number)) + 'i'

        if float(num2) % 1 == 0:
            num2 = str(int(float(num2)))

        result = '{} + {}'.format(num2, num1)
    else:
        number = float(num2[:-1])
        if number % 1 == 0:
            num2 = str(int(number)) + 'i'

        if float(num1) % 1 == 0:
            num1 = str(int(float(num1)))

        result = '{} + {}'.format(num1, num2)

    return result


def sub_complex(is_num1_complex: bool, is_num2_complex: bool, num1: str, num2: str) -> str:
    result = ''
    if is_num1_complex and is_num2_complex:
        number = float(num1) - float(num2)
        if number % 1 == 0:
            result = str(int(number)) + 'i'
        else:
            result = str(number) + 'i'
    elif is_num1_complex:
        number = float(num1)
        if number % 1 == 0:
            num1 = str(int(number)) + 'i'

        if float(num2) % 1 == 0:
            num2 = str(int(float(num2)))

        result = '{} - {}'.format(num2, num1)
    else:
        number = float(num2)
        if number % 1 == 0:
            num2 = str(int(number)) + 'i'

        if float(num1) % 1 == 0:
            num1 = str(int(float(num1)))

        result = '{} - {}'.format(num1, num2)

    return result


def mult_complex(is_num1_complex: bool, is_num2_complex: bool, num1: str, num2: str) -> str:
    result = ''
    number = float(num1) * float(num2)
    if number % 1 == 0:
        number = int(number)

    if is_num1_complex and is_num2_complex:
        result = str(number * (-1))
    else:
        result = f'{number}i'

    return result


def div_complex(is_num1_complex: bool, is_num2_complex: bool, num1: str, num2: str) -> str:
    result = ''
    number = float(num1) / float(num2)
    if number % 1 == 0:
        number = int(number)

    if is_num1_complex and is_num2_complex:
        result = str(number)
    elif is_num1_complex:
        result = f'{number}i'
    else:
        result = f'{number * (-1)}i'

    return result


# dct = {
#     'num1': '4.0',
#     'num2': '2.0i',
#     'operator': '-'
# }

# print(calculate_complex(dct))
