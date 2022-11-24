def sumComplex(dct: dict) -> dict:
    is_num1_complex = False
    is_num2_complex = False
    num1 = str(dct['num1'])
    num2 = str(dct['num2'])

    if num1[-1] == 'i':
        is_num1_complex = True

    if num2[-1] == 'i':
        is_num2_complex = True

    if is_num1_complex and is_num2_complex:
        number = float(num1[:-1]) + float(num2[:-1])
        if number % 1 == 0:
            dct['result'] = str(int(number // 1)) + 'i'
        else:
            dct['result'] = str(number) + 'i'
    elif is_num1_complex:
        number = float(dct['num1'][:-1])
        if number % 1 == 0:
            dct['result'] = str(int(number // 1)) + 'i'
        dct['result'] = '{} + {}'.format(num2, num1)
    else:
        number = float(dct['num2'][:-1])
        if number % 1 == 0:
            dct['result'] = str(int(number // 1)) + 'i'
        dct['result'] = '{} + {}'.format(num1, num2)

    return dct


def subComplex(dct: dict) -> dict:
    is_num1_complex = False
    is_num2_complex = False
    num1 = str(dct['num1'])
    num2 = str(dct['num2'])

    if num1[-1] == 'i':
        is_num1_complex = True

    if num2[-1] == 'i':
        is_num2_complex = True

    if is_num1_complex and is_num2_complex:
        number = float(num1[:-1]) - float(num2[:-1])
        if number % 1 == 0:
            dct['result'] = str(int(number // 1)) + 'i'
        else:
            dct['result'] = str(number) + 'i'
    elif is_num1_complex:
        number = float(dct['num1'][:-1])
        if number % 1 == 0:
            dct['result'] = str(int(number // 1)) + 'i'
        dct['result'] = '{} - {}'.format(num2, num1)
    else:
        number = float(dct['num2'][:-1])
        if number % 1 == 0:
            dct['result'] = str(int(number // 1)) + 'i'
        dct['result'] = '{} - {}'.format(num1, num2)

    return dct


# dct = {
#     'num1': '2.6i',
#     'num2': '3.6i'
# }

# print(subComplex(dct))
