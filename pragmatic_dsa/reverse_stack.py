from utils import utils as u
"""
Use a stack to reverse a string
"""


def string_reversal(word: str) -> str:
    stack = []
    final_string = ""
    for char in word:
        stack.append(char)

    length = u.get_length(stack)

    i = 0
    while i < length:
        final_string += stack.pop()
        i += 1
    return final_string


test_strings = [
    "TEST",
    "RACECAR",
    "MEEPLE"
]

for string in test_strings:
    print(string_reversal(string))
