from contacts import lst, search, add, change, delete

allowed_menu = list(range(6))

menu_items = {
    1: lst.main,
    2: search.main,
    3: add.main,
    4: change.main,
    5: delete.main,
}


def show_menu():
    print('''
Меню:
1. Список контактов
2. Поиск контакта
3. Добавить контакт
4. Изменить контакт
5. Удалить контакт
0. Выход    
    ''')


def select_menu():
    global allowed_menu
    show_menu()
    while True:
        try:
            menu_index = int(input('Введите пункт меню: '))
            if menu_index not in allowed_menu:
                raise ValueError
            return menu_index
        except ValueError:
            print(f'Допустимые значения: {allowed_menu}')


def main():
    global menu_items
    while True:
        ind = select_menu()
        if ind == 0:
            break
        menu_items[ind]()
