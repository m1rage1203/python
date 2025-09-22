num1 = int(input('Введите первое число '))
num2 = int(input('Введите второе число '))
operation = input('Выберите операцию (+, -, *, /, //, %, **, <, >, <=, >=, ==, !=, Другие операции('')) ')
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
result = None
if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/' and num2 != 0:
    result = num1 / num2
    print(result)
elif operation == '//' and num2 != 0:
    result = num1 // num2
    print(result)
elif operation == '%' and num2 != 0:
    result = num1 % num2
    print(result)
elif operation == '**':
    result = num1 ** num2
    print(result)
elif operation == '<':
    result = num1 < num2
    print(result)
elif operation == '<=':
    result = num1 < num2
    print(result)
elif operation == '>':
    result = num1 > num2
    print(result)
elif operation == '>=':
    result = num1 >= num2
    print(result)
elif operation == '==':
    result = num1 == num2
    print(result)
elif operation == '!=':
    result = num1 != num2
    print(result)
elif operation == 'Другие операции' or operation == '':
    operation2 = input('Введите другую операцию ')
    if operation2 == 'not':
        if num1 > 0 and not (num2 < 0):
            print('Оба числа положительные')
    if operation2 == '<<':
        result = num1 << num2
        print('Побитовый сдвиг влево', result)
    elif operation2 == '>>':
        result = num1 >> num2
        print('Побитовый сдвиг вправо', result)
    elif operation2 == '&':
        result = num1 & num2
        print('Побитовое И', result)
    elif operation2 == '|':
        result = num1 ^ num2
        print('Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ', result)
    elif operation2 == '|':
        result = ~num2
        print('Побитовое НЕ', result)
    elif operation2 == 'in':
        if num1 in b and num2 in b:
            print('Оба значения - цифры')
    elif operation2 == 'not in':
        if num1 not in b and num2 not in b:
            print('Оба значения - числа')
    elif operation2 == 'is':
        if num1 is num2:
            print('Оба значения одинаковы')
        else:
            print('не одинаковы')
    elif operation2 == 'is not':
        if num1 is num2:
            print('Значения разные')
        else:
            print('Одинаковы')
    
        
     