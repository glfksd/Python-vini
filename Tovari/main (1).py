"""Общее
1. Есть текстовый файл с данными (in.txt)
2. Прочесть в список экземпляров класса
3. Отсортировать по условию
4. Вывести в другой файл (out.txt)

Никита
Класс Товары
id Name Price
Пример файла
1 Сникерс 100
2 Марс 200
3 Аленка 150
4 Твикс 300

Отсортировать по цене
1 Сникерс 100
3 Аленка 150
2 Марс 200
4 Твикс 300"""


class Tovar:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self. price = price

def read_from_file(filename):
    calls = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            id, name, price = line.strip().split()
            calls.append(Tovar(id, name, price))
    return calls

def calcul(calls):
    return sorted(calls, key=lambda Tovar: Tovar.price)

def write_to_file(calls, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for Tovar in calls:
            file.write(f"{Tovar.id} {Tovar.name} {Tovar.price}\n")

calls = read_from_file('in.txt')
sorted_file = calcul(calls)
write_to_file(sorted_file, 'out.txt')

