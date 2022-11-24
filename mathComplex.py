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
        dct['result'] = str(float(num1[:-1]) + float(num2[:-1])) + 'i'
    elif is_num1_complex:
        dct['result'] = '{} + {}'.format(num2, num1)
    else:
        dct['result'] = '{} + {}'.format(num1, num2)

    number = float(dct['result'][:-1])
    if number % 1 == 0:
        dct['result'] = str(int(number // 1)) + 'i'

    print(dct)


# dct = {
#     'num1': '2i',
#     'num2': '3i'
# }

# sumComplex(dct)
