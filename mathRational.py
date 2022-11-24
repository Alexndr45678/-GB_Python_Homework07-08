def calculate(dct: dict)-> dict:
    if dct['operator'] == '+':
        dct['result']= float(dct['num1']) + float(dct['num2'])
    elif dct['operator'] == '-':
        dct['result']= float(dct['num1']) - float(dct['num2'])
    elif dct['operator'] == '*':
        dct['result']= float(dct['num1']) * float(dct['num2'])
    elif dct['operator'] == '/':
        dct['result']= float(dct['num1']) / float(dct['num2'])
    elif dct['operator'] == '^':
        dct['result']= float(dct['num1']) * float(dct['num1'])
    return dct
