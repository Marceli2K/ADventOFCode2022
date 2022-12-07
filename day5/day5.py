
import re
from time import sleep


def read_file():
    with open(r'C:\Users\LAB2\Desktop\AOC\day5\input.txt', 'r') as file:
        stacks_str, operations_str = file.read().split('\n\n')
        transposed = list(zip(*stacks_str.splitlines()))
        stacks = {}
        for x in transposed[1::4]:
            stack = list(c for c in x if c != ' ')
            key = stack.pop()
            stack.reverse()
            stacks[key] = stack
        operations = []
        for o in operations_str.splitlines():
            amount, key, to = re.findall(r'(\d+) from (\d+) to (\d+)', o).pop()
            operations.append((int(amount), key, to))
        return stacks, operations


def operatione(stacks, operations):
    for line in operations:
        move, frome, to = line
        # for i in range(move):
        try:
            stacks[to].extend(stacks[frome][-move:])
            print(stacks[frome][-move:])
            for i in range(move):
                stacks[frome].pop()
            print(stacks)
        except:
            pass
    for x in stacks:
        xx = stacks[x][-1].replace('\n', '')
        print(xx)
    return xx


if __name__ == '__main__':
    stacks, operations = read_file()
    x = (operatione(stacks, operations))
