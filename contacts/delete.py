from services.filedata import read_csv, rewrite_csv
from services.inputer import input_num


def delete(lst, contact_num):
    del lst[contact_num - 1]
    rewrite_csv(lst)


def main():
    lst = read_csv()
    contact_num = input_num(len(lst), 'Удаление контакта')
    delete(lst, contact_num)
    print(f'Контакт под номером {contact_num} удалён!')
