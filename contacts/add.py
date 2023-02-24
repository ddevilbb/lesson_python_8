from services import filedata
from services.inputer import input_contact


def add(contact):
    filedata.write_to_csv(contact)


def main():
    contact = input_contact()
    add(contact)
    print('Контакт добавлен!')
