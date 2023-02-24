filename = 'resources/phonebook.csv'


def write_to_csv(item):
    global filename
    print(";".join(item))
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{";".join(item)}\n')


def rewrite_csv(lst):
    global filename
    with open(filename, 'w+', encoding='utf-8') as f:
        for item in lst:
            f.write(f'{";".join(item[1:])}\n')


def read_csv():
    global filename
    with open(filename, 'r', encoding='utf-8') as f:
        result = []
        lines = f.read().splitlines()
        for i, value in enumerate(lines):
            lst = value.split(';')
            lst.insert(0, str(i + 1))
            result.append(lst)
        return result
