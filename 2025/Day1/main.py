def solve(filename):
    with open(filename) as f:
        num_pointer = 50
        counter_zero = 0
        for line in f:
            if line[0] == "L":
                # old protocoll
                num_pointer = (num_pointer - int(line[1:])) % 100
            elif line[0] == "R":
                # old protocoll
                num_pointer = (num_pointer + int(line[1:])) % 100
            else:
                # if there are empty lines ignore them
                continue

            if num_pointer == 0:
                counter_zero += 1
    
    print(f"The passcode is {counter_zero}")
    return counter_zero

def solve_prot(filename):
    num_pointer = 50
    result = 0
    with open(filename) as f:
        for line in f:
            direction = line[0]
            rotation = int(line[1:])

            for _ in range(rotation):
                if direction == "R":
                     num_pointer = (num_pointer + 1) % 100
                elif direction == "L":
                    num_pointer = (num_pointer - 1) % 100
                
                if num_pointer == 0:
                    result += 1
    
    print(f"using the new protocoll the passcode is: {result}")
    
    return result



if __name__ == "__main__":
    filename = "./Day1/input.txt"
    solve(filename)
    solve_prot(filename)