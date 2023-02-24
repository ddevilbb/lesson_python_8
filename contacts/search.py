from services import filedata
from helpers import print_formatter


def input_search():
    return input('Введите строку для поиска: ')


def search_string(search_str):
    print(search_str)
    lst = filedata.read_csv()
    return list(filter(lambda item: search_str in item, lst))


def main():
    search_str = input_search()
    lst = search_string(search_str)
    print_formatter.print_lst(lst)
