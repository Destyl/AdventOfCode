import numpy as np

def solve(filename):
    maxBanks = []
    with open(filename) as f:
        for line in f:
            line = np.array([x for x in line.rstrip()])
            res = int(''.join(maxBank(line, 12)))
            maxBanks.append(res)
            
    print(maxBanks)
    print(sum(maxBanks))

def maxBank(bank, missing):
    if missing <= 0:
        return np.array([])
    
    maxPointer = np.argmax(bank)
    diff = len(bank) - maxPointer
    if missing == 1:
        return [bank[maxPointer]]
    if missing >= diff:
        left = maxBank(bank[:maxPointer], missing - (len(bank) - maxPointer))
        right = bank[maxPointer:]
    else:
        left = np.array([bank[maxPointer]])
        right = maxBank(bank[maxPointer+1:], missing-1)
    
    res = [str(x) for x in np.concatenate((left, right))]
    return res


if __name__ == "__main__":
    filename = "2025/Day3/input.txt"
    solve(filename)