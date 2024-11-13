"""
Use a stack to reverse a string
"""


def string_reversal(word: str) -> str:
    stack = []
    final_string = ""
    for char in word:
        stack.append(char)

    length = len(stack)

    for i in range(length):
        final_string += stack.pop()
    return final_string


test_strings = [
    "TEST",
    "RACECAR",
    "MEEPLE"
]

for string in test_strings:
    print(string_reversal(string))
