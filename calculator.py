f = 'Введите первое число:  '
o = 'Введите операцию (+,-, /, *):  '
s = 'Введите второе число:  '
r = 'Результат: '
e = 'Ошибка'
v = 'Введите "Y", чтобы продолжить или любую клавишу, чтобы закончить:  '
prodolzhit ='Y'
while prodolzhit == 'Y':
    f_num = float(input(f))
    oper = input(o)
    sec_num = float(input(s))
    if oper == '+':
        print(r, f_num + sec_num)
    elif oper == '-':
        print(r, f_num - sec_num)
    elif oper == '/':
        print(r, f_num / sec_num)
    elif oper == '*':
        print(r, f_num * sec_num)
    else:
        print(e)
    prodolzhit = input(v)
