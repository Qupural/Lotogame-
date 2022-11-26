import random
from random import randint


class Cards:
    def __init__(self):
        self.data = []
        self.rows = 3
        self.cols = 9
        self.nums_in_row = 5

    def generate_unique_numbers(self,counte,minbound,maxbound):
        ret = []
        while counte != 0:
            a = randint(minbound,maxbound)
            if a in ret:
                pass
            else:
                ret.append(a)
                counte-=1
        return ret
        #используй библиотеку randint и цикл while, допиши добавление числа в список

    def cards(self):
        count = self.nums_in_row * self.rows
        uniques = self.generate_unique_numbers(count,1,90)


        for i in range(0, self.rows):
            tmp = []
            count = 5
            uniques.sort()
            while count != 0:
                qwe= random.choice(uniques)
                tmp.append(qwe)
                uniques.remove(qwe)
                count -= 1
           # tmp = сортируем uniques и создем три списка по 5 чисел из списка uniques
            empty_nums_count = self.cols - self.nums_in_row
            for j in range(0, empty_nums_count):
                random_index_1 = randint(0, len(tmp) - 1)
                tmp.insert(random_index_1, 0)
                #добавляем нули, выбирая рандомно индекс из tmp и вставляя по этому индексу 0
            self.data += tmp
        return self.data
    def cards_form(self, name ):
        delimiter = '--------------------------'
        if (name == 'Игрок1') or (name == 'Игрок2') or (name == 'Игрок!'):
            delimiter_1 = '-' * 10
        else :
            delimiter_1 = '-' * 8
        ret = delimiter_1 + name + delimiter_1 + '\n'
        for index, num in enumerate(self.data):
            if num == 0:
                ret += '  '
            elif num == -1:
                ret += '-'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % 9 == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter
