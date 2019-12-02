from typing import List

DEBUG = False


def program_alarm(intcode: List[int], debug: bool = False) -> List[int]:
    for i in range(len(intcode)):

        if debug:
            print(f"step {i} state: {intcode}")

        if i % 4 == 0:
            op_code = intcode[i]
            if debug:
                print(f"\toper_code is {op_code}")

            if op_code == 1 or op_code == 2:
                var1 = intcode[intcode[i + 1]]
                var2 = intcode[intcode[i + 2]]
                offset = intcode[i + 3]

                if debug:
                    print(f"\tvar_1 is {var1}")
                    print(f"\tvar_2 is {var2}")
                    print(f"\toffset is {offset}")

                if op_code == 1:
                    result = var1 + var2
                elif op_code == 2:
                    result = var1 * var2

                intcode[offset] = result

                if debug:
                    print(f"\tresult is {result}")

            elif op_code == 99:
                break

    return intcode


def open_file() -> List[int]:
    with open("input2.txt", "r") as f:
        input_text = f.readline()
        int_code_list = list(map(int, str.split(input_text, ",")))
        return int_code_list


test1 = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
test2 = [1, 0, 0, 0, 99]
test3 = [2, 3, 0, 3, 99]
test4 = [2, 4, 4, 5, 99, 0]
test5 = [1, 1, 1, 4, 99, 5, 6, 0, 99]


# print("*****test 1")
# print(program_alarm(test1))
# print("*****test 2")
# print(program_alarm(test2))
# print("*****test 3")
# print(program_alarm(test3))
# print("*****test 4")
# print(program_alarm(test4))
# print("*****test 5")
# print(program_alarm(test5))


# solution to question one
int_code_list = open_file()
int_code_list[1] = 12
int_code_list[2] = 2
print(f"solution to question one: {program_alarm(int_code_list, DEBUG)[0]}")

desired_output = 19690720

for noun in range(99):
    for verb in range(99):
        int_codes = open_file()
        int_codes[1] = noun
        int_codes[2] = verb
        result = program_alarm(int_codes)[0]
        if result == desired_output:
            print(f"noun: {noun}, verb: {verb}, result: {result}")
            print(f"100 * noun + verb = {100 * noun + verb}")
