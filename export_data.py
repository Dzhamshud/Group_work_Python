
def read_csv_file() -> dict:
    with open('data.csv', encoding='utf-8') as f:
        data = []
        st = f.readlines()
        for i in st:
            st_in = i.split(';')
            tpl = tuple(j.strip() for j in st_in)
            data.append(tpl)

    return data

def read_txt_file():
    file_name = "data.txt"
    data = list()
    with open(file_name, encoding='utf-8') as file:

        current = file.readline()
        while len(current) > 0:
            current_lst = []
            while current != "\n" and len(current) > 0:
                current = current.replace("\n", "")
                current_lst.append(current)
                current = file.readline()
            data.append(tuple(current_lst))
            current = file.readline()

    return data
