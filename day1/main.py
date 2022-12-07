
####https://adventofcode.com/2022/day/1
sum =0
numb = 0
list = []

with open("input", "r") as txt_file:
    for x in txt_file:
        if x != '\n':
            numb = numb + int(x)
        if x == '\n':
            list.append(numb)
            numb = 0

for x in range(3): #sumowanie trzech największych liczb z poprzedniego podzbioru
    sum = sum + (max(list))
    list.pop(list.index(max(list)))
    print(sum)
