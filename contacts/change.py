from services.filedata import read_csv, rewrite_csv
from services.inputer import input_contact, input_num


def change(lst, contact_num, contact_data):
    contact_data.insert(0, contact_num)
    lst[contact_num - 1] = contact_data
    rewrite_csv(lst)


def main():
    lst = read_csv()
    contact_num = input_num(len(lst), 'Изменение контакта')
    contact_data = input_contact()
    change(lst, contact_num, contact_data)
    print(f'Контакт под номером {contact_num} изменён!')
