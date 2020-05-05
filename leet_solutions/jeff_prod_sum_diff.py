# This problem requires the return of the difference
# between the product of a number's digits and the sum


def subtractProductAndSum(n: int) -> int:
    n_str = str(n)
    n_list = [int(i) for i in n_str]
    digit_prod = 1
    digit_sum = 0
    for num in n_list:
        digit_prod *= num
        digit_sum += num
    return digit_prod - digit_sum
