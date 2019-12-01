def calc_fuel(mass):
    # no such thing as negative fuel
    return max((mass // 3) - 2, 0)


def calc_fuel_recursively(fuel):
    fuel_required = calc_fuel(fuel)
    # base case, no more fuel needed
    if fuel_required == 0:
        return 0
    else:
        return fuel_required + calc_fuel_recursively(fuel_required)


with open('input.txt') as f:
    fuel_required = sum(map(calc_fuel_recursively, map(int, f.readlines())))


print(fuel_required)
print(calc_fuel_recursively(14))
print(calc_fuel_recursively(1969))
print(calc_fuel_recursively(100756))
