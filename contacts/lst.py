from services import filedata
from helpers import print_formatter


def main():
    lst = filedata.read_csv()
    print_formatter.print_lst(lst)
