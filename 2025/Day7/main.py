import re

def solve(filename):
    with open(filename) as f:
        data = f.readlines()
        beam_positions = [data[0].find("S")]
        counter = 0
        for line in data[1:]:
            new_beam_positions = []
            for beam in beam_positions:
                splitters = [m.start(0) for m in re.finditer("\^", line)]
                if beam in splitters:
                    counter +=1
                    if beam - 1 not in new_beam_positions:
                        new_beam_positions.append(beam - 1)
                    if beam + 1 not in new_beam_positions:
                        new_beam_positions.append(beam + 1)
                elif beam not in new_beam_positions:
                    new_beam_positions.append(beam)
            beam_positions = new_beam_positions

        print(beam_positions)
        print(len(beam_positions))
        print(f"counter: {counter}")

def solve2(filename):
    with open(filename) as f:
        data = f.readlines()
        beam_positions = [int(x == 'S') for x in data[0]]
        for line in data[1:]:

            new_beam_pos = [0] * len(line)
            splitters = [m.start(0) for m in re.finditer("\^", line)]
            for beam_pos, beam_count in enumerate(beam_positions):
                if beam_count > 0:
                    if beam_pos in splitters:
                        new_beam_pos[beam_pos - 1] += beam_count
                        new_beam_pos[beam_pos + 1] += beam_count
                    else:
                        new_beam_pos[beam_pos] += beam_count
            beam_positions = new_beam_pos

        print(beam_positions)
        print(sum(beam_positions))

if __name__ == "__main__":
    filename = "2025/Day7/input.txt"
    # filename = "2025/Day7/test0.txt"
    solve2(filename)