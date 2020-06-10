def generate_parentheses(n):
    if n <= 0:
        return []

    def recurse(i=0, j=0, p=[]):
        if i == n:
            to_close = [")"] * (2 * n - len(p))
            yield "".join(p + to_close)
            return

        for k in range(max(i, j), 2 * i + 1):
            to_close = [")"] * (k - len(p))
            yield from recurse(i + 1, k + 1, p + to_close + ["("])

    return recurse()
