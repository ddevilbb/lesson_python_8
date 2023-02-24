def print_format(*args):
    first, *fields, last = args
    print(f'{first}'.ljust(4), end='')
    for field in fields:
        print(f'{field}'.ljust(20), end='')
    print(f'{last}'.ljust(12), end='\n')


def print_lst(lst):
    print_format('№', 'Фамилия', 'Имя', 'Отчество', 'Телефон')
    for item in lst:
        print_format(*item)
