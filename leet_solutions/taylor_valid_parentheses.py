pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
}


def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
            continue

        if not stack or pairs[c] != stack[-1]:
            return False

        stack.pop()

    return len(stack) == 0
