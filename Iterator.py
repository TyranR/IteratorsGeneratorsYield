# Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.

import json
from pprint import pprint


class MyIter:
    def __init__(self, end, countries):
        self.url = 'https://en.wikipedia.org/wiki/'
        self.name = countries[0]
        self.start = 0
        self.end = end - 1
        self.all = countries

    def __iter__(self):
        return self

    def __next__(self):
        self.name = self.all[self.start]
        prepare = self.name.split()
        final = '_'.join(prepare)
        self.url = 'https://en.wikipedia.org/wiki/' + final
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.name, self.url


def countries_collect(data):
    """
    Собираем страны из JSON
    """
    all_countries = []
    for each in data:
        all_countries.append(each['name']['common'])
    return all_countries


def main():
    with open('countries.json', encoding='utf-8') as file:
        json_data = json.load(file)
    countries = countries_collect(json_data)
    calc_countries = len(countries)
    with open('result.txt', encoding='utf-8', mode='w') as file:
        file.write("Let's do it!\n\n")
    for item in MyIter(calc_countries, countries):
        with open('result.txt', encoding='utf-8', mode='a') as file:
            file.write(f'{item[0]} - {item[1]}\n')
        # print(item)


main()
