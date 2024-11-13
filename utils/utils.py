"""
Created functions to try not using premade Python functions where possible.
Requirement of the openac dsa module, so worth applying to other learning
"""


def get_length(item) -> int:
    count = 0
    for i in item:
        count += 1
    return count
