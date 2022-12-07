
alphabet = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
        'i' : 9,
        'j' : 10,
        'k' : 11,
        'l' : 12,
        'm' : 13,
        'n' : 14,
        'o' : 15,
        'p' : 16,
        'q' : 17,
        'r' : 18,
        's' : 19,
        't' : 20,
        'u' : 21,
        'v' : 22,
        'w' : 23,
        'x' : 24,
        'y' : 25,
        'z' : 26,
        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52


    }
lista_main = []

def split(s):
	# Find the half, rounding up
    half = int((len(s) / 2))
    first = s[:half]
    second = s[half:]
    return [first, second]


def part1(txt_file):
    inter = 0
    for x in txt_file:
        str1, str2 = split(x)
        lista_main.extend(set(str1)  & set(str2))
        for x in lista_main:
            inter = inter + int(alphabet.get(x))
        return inter

def part2(txt_file):
    letters= []
    numbers = []
    data = txt_file.read().split('\n')
    for data1, data2, data3 in zip(data[0::3], data[1::3], data[2::3]):
        letters.extend(set(data1) & set(data2) & set(data3))
        numbers.append(alphabet.get(letters[-1]))
    return(sum(numbers))

with open("input", "r") as txt_file:
    #print(part1(txt_file))
    print(part2(txt_file))
