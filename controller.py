def is_complex(dct: dict):
    print(dct['num1'][-1])
    if str(dct['num1'])[-1] == 'i' or str(dct['num2'])[-1] == 'i':
        print('complex')
    else:
        print('rational')
