import numpy as np

def solve(filename):
    with open(filename) as f:
        total = 0
        rolls_grid = [list(line.rstrip()) for line in f]
        while(True):
            count_grid = calc_grid(rolls_grid=rolls_grid)
            
            count = 0
            for y in range(len(rolls_grid)):
                for x in range(len(rolls_grid[y])):
                    if count_grid[y+1, x+1] < 4:
                        count += 1
                        rolls_grid[y][x] = 'x'
            print(count)
            if count == 0:
                break
            
            total += count
        print(total)
            

def calc_grid(rolls_grid):
    count_grid = np.zeros((len(rolls_grid)+2, len(rolls_grid[0])+2)) + 100
    count_grid[1:-1,1:-1] = 0
    
    for y in range(len(rolls_grid)):
        for x in range(len(rolls_grid[y])):
            if rolls_grid[y][x] == '@':
                count_grid[y:y+3, x:x+3] += 1
                count_grid[y+1,x+1] -= 1
            else:
                count_grid[y+1,x+1] = 100
    
    return count_grid



if __name__ == "__main__":
    filename = "2025/Day4/input.txt"
    solve(filename)