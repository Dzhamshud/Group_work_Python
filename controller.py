from export_data import read_csv_file, read_txt_file
from import_data import write_txt_file, write_csv_file
import find_peaple as fp

# data = [('Иванов', 'Иван', 'Васильевич', 'слесарь', 'слесарный отдел', 'Рога и копыта'), (), (), ()]
# data = [
#     {
#         'surname': 'Иванов',
#         'name': 'Иван',
#         ...
#     }
# ]

def print_data(data):
    for i in range(len(data)):
        # print(data[i])
        print(f'Фамилия: {data[i][0]} \nИмя: {data[i][1]} \nОрганизация: {data[i][2]} \nДолжность: {data[i][3]} \nГруппа: {data[i][4]} \nТелефон: {data[i][5]}')
        print()

def read_data(type):
    if type == 'csv':
        data = read_csv_file()
        return data
    elif type == 'txt':
        data = read_txt_file()
        return data

def write_data(data, type):
    if type == 'csv':
        write_csv_file(data)
    elif type == 'txt':
        write_txt_file(data)

def run():
    data = read_data(type='txt')
    print_data(data)
    find_data = fp.go(data)
    print()
    print_data(find_data)
    write_data(find_data, type='txt')
