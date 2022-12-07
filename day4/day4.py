lista = []


def checker_part1(lista):
    lista1 = []
    lista2 = []
    counter = 0
    for x in lista:
        a, b = x[0]
        c, d = x[1]
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if a <= c <= d <= b or c <= a <= b <= d or (a == b and c <= a <= d):
            counter = counter + 1
        else:
            pass
    return counter


def checker_part2(lista):
    lista1 = []
    lista2 = []
    counter = 0
    for x in lista:
        a, b = x[0]
        c, d = x[1]
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if (a <= c and b >= d and b >= c and a <= d) or (a <= c and b <= d and b >= c and a <= d) or (a >= c and b >= d and b >= c and a <= d) or (a >= c and b <= d and b >= c and a <= d):
            counter = counter + 1
        else:
            pass
    return counter


with open(r'C:\Users\LAB2\Desktop\AOC\day4\input.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        str1, str2 = line.split(',')
        str1 = str1.split('-')
        str2 = str2.split('-')
        lista.append([str1, str2])
    print(checker_part2(lista))
