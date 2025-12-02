import math
import re

# using arithmetic (only works for part 1)
def solve(filename):
    matches = []
    with open(filename) as f:
        data = f.read()
        ranges = data.split(",")
        for r in ranges:
            id_min, id_max = r.split("-")
            id_min = int(id_min)
            id_max = int(id_max)

            for id in range(id_min, id_max+1):
                # interesting arithmetic approach: 
                if (int(math.log10(id))+1) % 2 == 0:
                    N = 10 ** int(math.log10(id)//2 +1)
                    split0 = id // N
                    split1 = id % N
                    if split0 == split1:
                        matches.append(id)
    match_sum = sum(matches)
    print(matches)
    print(match_sum)

# using regex (for part 2)
def solve2(filename):
    matches = []
    pattern = r"^(\d+)\1+$"

    with open(filename) as f:
        data = f.read()
        ranges = data.split(",")
        for r in ranges:
            id_min, id_max = r.split("-")
            id_min = int(id_min)
            id_max = int(id_max)

            for id in range(id_min, id_max+1):
                id_str = str(id)
                x = re.findall(pattern, id_str)
                if len(x) != 0:
                    matches.append(id)

    match_sum = sum(matches)
    print(matches)
    print(match_sum)


if __name__ == "__main__":
    filename = "2025/Day2/input.txt"
    # filename = "2025/Day2/test0.txt"

    solve2(filename)