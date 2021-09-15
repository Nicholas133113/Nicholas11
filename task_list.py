task_list = []

print('Здравствуй дорогой пользователь!')

def update_task_is_done(number):
    task = task_list[number]
    task["is_done"] = not task["is_done"]
    return task

def valid_task_number(number):
    return number.isdigit() and 0 < int(number) <= len(task_list)

def strike(text):
    i = 0
    new_text = ''
    while i < len(text):
        new_text = new_text + (text[i] + u'\u0336')
        i = i + 1
    return(new_text)

def strike_task(task):
    return strike(task["text"]) if task["is_done"] else task["text"]

def yes_no_task_choice(number, task, action):
    y = input(f' Вы хотите добавить еще одну задачу? (y/n) ')
    return y in ('Y', 'y')

def add_task(text):
    task = {
        "text": text,
        "is_done": False
    }
    task_list.append(task)
    return task

def update_task_text(number, text):
    task = task_list[number]
    task["text"] = text
    return task

def print_task_list():
    i = 1
    print('Список задач:')
    for task in task_list:
        print(f'{i}. {strike_task(task)}')
        i += 1
    return True
    
def print_delete_task_list():
    while len(task_list):
        print_task_list()
        number = input('Введите номер задачи которую хотите удалить: ')
        if not valid_task_number(number):
            print('Неверный номер задачи, попробуйте еще раз\n')
            continue
        number = int(number)
        task = delete_task(number - 1)
        if not yes_no_task_choice(number, task, 'delete'):
            break
    else: 
        print('Нет списка задач')
    return True

def print_add_task_list():
    while True:
        print_task_list()
        text = input('Введите новую задачу: ')
        task = add_task(text)
        if not yes_no_task_choice(len(task_list), task, 'add'):
            break
    return True

def print_update_task_list_text():
    while True:
        print_task_list()
        number = input('Введите номер задачи, который хотите изменить: ')
        if not valid_task_number(number):
            print('Неверный номер задачи, попробуйте еще раз\n')
            print_task_list()
            continue
        number = int(number)
        text = input('Введите текст, на который хотите изменить: ')
        task = update_task_text(number - 1, text)
        if not yes_no_task_choice(number, task, 'delete'):
            break
    return True
    
def print_update_task_list_is_done():
    while True:
        print_task_list()
        number = input('Введите номер задачи которую хотите отметить: ')
        if not valid_task_number(number):
            print('Неверный номер задачи, попробуйте еще раз\n')
            print_task_list()
            continue
        number = int(number)
        task = update_task_is_done(number - 1)
        if not yes_no_task_choice(number, task, 'mark'):
            break
    return True

def delete_task(number):
    task = task_list.pop(number)
    return task

def task_list_exit():
    y = input('Уверены, что хотите выйти из такой крутой программы? (y/n) ')
    if y in ('y', 'Y'):
        print('Досвидания дорогой пользователь! Возвращайтесь скорее!')
        exit()

choices = {
    "1": print_add_task_list,
    "2": print_task_list,
    "3": print_update_task_list_text,
    "4": print_update_task_list_is_done,
    "5": print_delete_task_list,
    "0": task_list_exit
}

menu = """

1. Добавить новую задачу
2. Показать список задач
3. Обновить задачу
4. Отметить задачу
5. Удалить задачу
0. Выйти
"""

while True:
    menu_number = input(menu)
    choice = choices.get(menu_number)
    if not choice:
        print('Неправильный номер меню, попробуйте еще раз')
        continue
    choice()

    
