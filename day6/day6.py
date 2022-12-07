
import re
from time import sleep


def read_file():
    with open(r'C:\Users\LAB2\Desktop\AOC\day6\input.txt', 'r') as file:
        str1 = file.readlines()[0].replace('\n', '')
    return str1


def ex1(str1):
    lista = []
    for x in str1:
        lista.extend(x)
    for i, ii in enumerate(lista):
        if lista[i] != lista[i+1] and lista[i] != lista[i+2] and lista[i+1] != lista[i+2] and lista[i] != lista[i+3] and lista[i+1] != lista[i+3] and lista[i+2] != lista[i+3]:
            print(ii)
            print(i+3+1)
            break


def ex2(str1):
    lista = []
    for x in str1:
        lista.extend(x)
    for i, ii in enumerate(lista):
        x = lista[i:i+14]
        import collections
        if len([item for item, count in collections.Counter(x).items() if count > 1]) == 0:
            print(i+13+1)
            print([item for item, count in collections.Counter(
                x).items() if count > 1])

            pass


        #print([item for item, count in collections.Counter(x).items() if not count > 1])
if __name__ == '__main__':
    str1 = read_file()
    ex2(str1)
