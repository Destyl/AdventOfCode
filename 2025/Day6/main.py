from functools import reduce
import operator as op
import numpy as np
import re

def solve(filename):
    with open(filename) as f:
        ws_numbers = []
        for line in f:
            if line[0] != '+' and line[0] != '*':
                ws_numbers.append(list(map(int, re.findall(r"\S+",line.rstrip()))))
            else:
                ws_operations = re.findall(r"\S+",line.rstrip())
        ws_numbers = np.array(ws_numbers).T
        results = []
        for idx in range(len(ws_operations)):
            if ws_operations[idx] == '+':
                results.append(sum(ws_numbers[idx]))
            elif ws_operations[idx] == '*':
                results.append(reduce(op.mul, ws_numbers[idx]))
        print(sum(results))

def solve2(filename):
    with open(filename) as f:
        ws_numbers = []
        for line in f:
            if line[0] != '+' and line[0] != '*':
                ws_numbers.append(list(line.replace("\n", "")))
            else:
                ws_operations = re.findall(r"\S+",line.rstrip())
        ws_numbers = np.array(ws_numbers).T
        
        results = []
        line_pointer = 0
        for idx in range(len(ws_operations)):
            temp = []
            while(True):
                if line_pointer == len(ws_numbers):
                    if ws_operations[idx] == '+':
                        results.append(sum(temp))
                    elif ws_operations[idx] == '*':
                        results.append(reduce(op.mul, temp))
                    break
                num = ''.join(ws_numbers[line_pointer]).strip()
                if num == '':
                    if ws_operations[idx] == '+':
                        results.append(sum(temp))
                    elif ws_operations[idx] == '*':
                        results.append(reduce(op.mul, temp))
                    line_pointer +=1
                    break
                else:
                    temp.append(int(num))
                line_pointer +=1
        print(sum(results))


if __name__ == "__main__":
    filename = "2025/Day6/input.txt"
    solve2(filename)