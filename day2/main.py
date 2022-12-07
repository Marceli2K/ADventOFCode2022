# A --> KAMIEN --> X 1
# B --> PAPIER --> Y 2
# C --> NOZYCZKI --> Z 3
# 0 przegrana. 3 remis, 6 wygrana
list=[]

def winner(lista):
    suma = 0
    for x in lista:
        if x[0] == x[1]: suma = suma + 3
        if (x[0] == 'A' and x[1] == 'B') or (x[0] == 'C' and x[1] == 'A') or (x[0] == 'B' and x[1] == 'C'):
                suma = suma + 6
        else:
            suma = suma
        if x[1] == 'A': suma = suma + 1
        if x[1] == 'B': suma = suma + 2
        if x[1] == 'C': suma = suma + 3
    return suma

def winner2(lista):
    suma = 0
    for x in lista:
        if x[1] == 'X':
            if x[0] == 'A': x[1] = 'C'
            elif x[0] == 'B': x[1] = 'A'
            elif x[0] == 'C': x[1] = 'B'
        elif x[1] == 'Y':
            if x[0] == 'A': x[1] = 'A'
            elif x[0] == 'B': x[1] = 'B'
            elif x[0] == 'C': x[1] = 'C'
        elif x[1] == 'Z':
            if x[0] == 'A': x[1] = 'B'
            elif x[0] == 'B': x[1] = 'C'
            elif x[0] == 'C': x[1] = 'A'
        print(x[0], x[1])
        if x[0] == x[1]: suma = suma + 3
        if (x[0] == 'A' and x[1] == 'B') or (x[0] == 'C' and x[1] == 'A') or (x[0] == 'B' and x[1] == 'C'):
                suma = suma + 6
        else:
            suma = suma
        if x[1] == 'A': suma = suma + 1
        if x[1] == 'B': suma = suma + 2
        if x[1] == 'C': suma = suma + 3
    return suma
#second stage
# x przegrana
# y remis
# z wygrana
with open("input", "r") as txt_file:
    for x in txt_file:
        first, second = x.split(" ")
        if second == "X\n":  list.append([first, "X"])
        if second == "Y\n":  list.append([first, "Y"])
        if second == "Z\n":  list.append([first, "Z"])


    suma = winner2(list)
    print(suma)


