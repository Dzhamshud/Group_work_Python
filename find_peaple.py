
def go(data):
    new_data = []
    find_data = input('Введите ключевое значение поиска: ')
    for person_data in data:
        for local_data in person_data:
            if find_data.lower() in local_data.lower():
                new_data.append(person_data)
                break
    return new_data
