# 221RDB085 Rudolfs Saukums 12. Grupa
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    openinig_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            openinig_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            if not openinig_brackets_stack or openinig_brackets_stack[-1].char + next not in ["()", "[]", "{}"]:
                return i + 1
            openinig_brackets_stack.pop()
    if not openinig_brackets_stack:
        return "Success"
    return openinig_brackets_stack[-1].position


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()

