def combinations(array, n):
    if n <= 0:
        return

    for i in range(len(array)):
        if n == 1:
            yield [array[i]]
            continue

        for res in combinations(array[i+1:], n - 1):
            yield [array[i]] + res
