"""
Locate the first duplicated value inside an array.
There will always be on duplicate
requirement of O(N)
"""


def find_duplicate(values: list) -> str:
    log = {}
    for value in values:
        if value in log:
            return value
        else:
            log[value] = 1


test_arrays = [
    ["a", "b", "c", "d", "c", "e"],
    ["a", "a", "c", "d", "c", "e"],
    ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vxy", "z", "abcd", "abc"],
]

for array in test_arrays:
    print(find_duplicate(array))
