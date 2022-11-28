
def write_txt_file(data: list):
    file_name = "res_find.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        for record in data:
            for string in record:
                file.writelines(string + "\n")
            file.writelines("\n")



def write_csv_file(data: list):
    st = ''
    for el in data:
        for j in el:
            st += j + ';'
        st = st[:-1] + '\n'

    with open('res_find.csv', 'w', encoding='utf-8') as f:
        f.write(st)
