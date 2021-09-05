print ('Здравствуй дорогой пользователь')
list1 = input('Введите информацию, в которую необходимо внести изменения:')
while 1 : 
    operation = input(' \n1. добавить значение в список  \n2. замена значения в строке \n3. сделать все буквы в строке заглавными \n4. сделать все буквы строчными \n5. сделать первую букву заглавной  \n6. вывеси информацию на экран \n7. посчитать количество символов в строке \n8. Вы желаете выйти? \n:')
    if  operation.isdigit() and '1'<=operation<='8':
        if operation == '8':
            question = input('Вы желаете выйти? (y/n)')
            if question == 'y':
                print('До свидания дорогой пользователь.')
                break
            elif question == 'n':
                continue  
        elif operation == '1':
            list2 =input('Введите значение:')
            list1 = list1+list2
            print (list1)
            question = input('Вы желаете выйти? (y/n)')
            if question == 'y':
                print('До свидания дорогой пользователь.')
                break
            elif question == 'n':
                continue  
        elif operation == '2':
            a = input('в каком значении  хотите внести изменение:')
            b = input ('на какое значение хотите изменить:')
            list3 = list1.replace(a,b)
            list1=list3
            print(list1)
            question = input('Вы желаете выйти? (y/n)')
            if question == 'y':
                print('До свидания дорогой пользователь.')
                break
            elif question == 'n':
                continue  
        elif operation == '3':
            list4=list1.upper()
            list1=list4
            print(list1)
            question = input('Вы желаете выйти? (y/n)')
            if question == 'y':
                print('До свидания дорогой пользователь.')
                break
            elif question == 'n':
                continue  
        elif operation == '4':
            list5=list1.lower()
            list1=list5
            print(list1)
            question = input('Вы желаете выйти? (y/n)')
            if question == 'y':
                print('До свидания дорогой пользователь.')
                break
            elif question == 'n':
                continue  
        elif operation == '5':
            list6 = list1.capitalize()
            list1=list6
            print (list6)
            question = input('Вы желаете выйти? (y/n)')
            if question == 'y':
                print('До свидания дорогой пользователь.')
                break
            elif question == 'n':
                continue
        elif operation == '6':
            print (list1)
            question = input('Вы желаете выйти? (y/n)')
            if question == 'y':
                print('До свидания дорогой пользователь.')
                break
            elif question == 'n':
                continue
        elif operation == '7':
            print(len(list1))
            question = input('Вы желаете выйти? (y/n)')
            if question == 'y':
                print('До свидания дорогой пользователь.')
                break
            elif question == 'n':
                continue
    else:
        print ('Error, ВВОДИТЕ ЦИФРЫ ОТ 1 ДО 8')
        continue
