import functools as ft
import itertools as it

from typing import List

p1 = 112233
p2 = 123444
p3 = 111122
p4 = 543214


def listify(number: int) -> List:
    return [int(c) for c in str(number)]


def is_monotic(sequence: int) -> bool:
    def _gen_seq():
        zipped_seq = it.zip_longest(listify(sequence), listify(sequence)[1:])
        for cur_val, next_val in zipped_seq:
            if next_val is not None:
                yield cur_val <= next_val

    return all(list(_gen_seq()))


def contains_pair(sequence: int) -> bool:
    def _gen_seq():
        for key, grp in it.groupby(listify(sequence)):
            items = list(grp)
            if len(items) == 2:
                yield True

    return any(list(_gen_seq()))


def contains_only_pair_groups(sequence: int) -> bool:
    def _gen_seq():
        for key, grp in it.groupby(listify(sequence)):
            items = list(grp)
            if len(items) % 2 == 0:
                yield True

    return any(list(_gen_seq()))


def is_valid_password(sequence: int) -> bool:
    if is_monotic(sequence):
        if contains_pair(sequence):
            if contains_only_pair_groups(sequence):
                return True


assert is_monotic(p1) == True
assert is_monotic(p2) == True
assert is_monotic(p3) == True
assert is_monotic(p4) == False

assert contains_pair(p1) == True
assert contains_pair(p2) == False
assert contains_pair(p3) == True
assert contains_pair(p4) == False

assert contains_only_pair_groups(p1) == True
assert contains_only_pair_groups(p2) == False
assert contains_only_pair_groups(p3) == True
assert contains_only_pair_groups(p4) == False

valid_passwords = 0
for i in range(372037, 905157):
    if is_valid_password(i):
        valid_passwords += 1
print(valid_passwords)
