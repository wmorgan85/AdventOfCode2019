from typing import List, Tuple


class WireCoords:
    def __init__(self):
        self.current_position = (0, 0)
        self.current_step = 0
        self.positions = {self.current_position}
        self.first_visited = {self.current_position: self.current_step}

    def __repr__(self):
        return f"({self.current_position[0]}, {self.current_position[1]})"

    def move(self, instruction: str) -> None:
        self.current_step += 1
        x = self.current_position[0]
        y = self.current_position[1]
        if instruction == "L":
            self.current_position = (x - 1, y)
        elif instruction == "R":
            self.current_position = (x + 1, y)
        elif instruction == "U":
            self.current_position = (x, y + 1)
        elif instruction == "D":
            self.current_position = (x, y - 1)
        else:
            pass
        if self.current_position not in self.positions:
            self.positions.add(self.current_position)
            self.first_visited[self.current_position] = self.current_step


def calc_manhattan_dist(coord: Tuple) -> int:
    return abs(coord[0]) + abs(coord[1])


def run_instructions(instr_set: List) -> WireCoords:
    wire_coords = WireCoords()
    for instr in instr_set:
        for i in range(int(instr[1:])):
            wire_coords.move(instr[0])
    return wire_coords


def find_nearest_cross(i1: List, i2: List) -> int:

    wire1 = run_instructions(i1)
    wire2 = run_instructions(i2)

    overlap = [
        pos for pos in wire1.positions if pos in wire2.positions and pos != (0, 0)
    ]

    return min(map(calc_manhattan_dist, overlap))


def find_minimum_cross(i1: List, i2: List) -> int:
    wire1 = run_instructions(i1)
    wire2 = run_instructions(i2)

    overlap = [
        pos for pos in wire1.positions if pos in wire2.positions and pos != (0, 0)
    ]

    step1 = [wire1.first_visited.get(pos) for pos in overlap]
    step2 = [wire2.first_visited.get(pos) for pos in overlap]
    steps = [x + y for x, y in zip(step1, step2)]

    return min(steps)


set_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
set_2 = "U62,R66,U55,R34,D71,R55,D58,R83"
set_3 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
set_4 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

instr_set_1 = str.split(set_1, ",")
instr_set_2 = str.split(set_2, ",")
instr_set_3 = str.split(set_3, ",")
instr_set_4 = str.split(set_4, ",")

assert find_nearest_cross(instr_set_1, instr_set_2) == 159
assert find_nearest_cross(instr_set_3, instr_set_4) == 135
assert find_minimum_cross(instr_set_1, instr_set_2) == 610
assert find_minimum_cross(instr_set_3, instr_set_4) == 410

with open("input3.txt") as f:
    instr_a = str.split(f.readline(), ",")
    instr_b = str.split(f.readline(), ",")
    print(f"Nearest cross is {find_nearest_cross(instr_a, instr_b)}")
    print(f"Minimum cross is {find_minimum_cross(instr_a, instr_b)}")

