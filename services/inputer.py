def input_contact():
    while True:
        try:
            lst = input('Введите фамилию, имя, отчество, номер телефона через пробел: ').split()
            if len(lst) < 4:
                raise ValueError
            return lst
        except ValueError:
            print('Введены не все данные!')


def input_num(contacts_cnt, operation_name):
    while True:
        try:
            contact_num = int(input(f'{operation_name}. Введите порядковые номер контакта для : '))
            if contact_num < 0 or contact_num > contacts_cnt:
                raise ValueError
            return contact_num
        except ValueError:
            print(f'Допустимые значения: от 1 до {contacts_cnt}')
