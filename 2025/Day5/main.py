def solve(filename):
    ranges = []
    ids = []
    with open(filename) as f:
        a = False
        for line in f:
            if line == "\n":
                a = True
                continue
            line = line.rstrip()
            if not a:
                r0,r1 = line.split('-')
                ranges.append([int(r0),int(r1)])
            else:
                ids.append(int(line))

    temp_ranges = ranges
    temp_ranges.sort(key = lambda r: r[0])
    ranges = [temp_ranges[0]]
    for current in temp_ranges:
        prev = ranges[-1]
        if current[0] <= prev[1]:
            prev[1] = max(current[1], prev[1])
        else:
            ranges.append(current)
    print(ranges)
    fresh_counter = 0
    for id in ids:
        for r in ranges:
            if id > r[1]:
                continue
            if id < r[0]:
                continue
            fresh_counter += 1

    print(f"Fresh: {fresh_counter}")

    total_fresh = 0
    for r in ranges:
        total_fresh += r[1] - r[0] +1 
    print(f"total fresh: {total_fresh}")


if __name__ == "__main__":
    filename = "2025/Day5/input.txt"
    solve(filename)