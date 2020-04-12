import itertools as it
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for (i0, x), (i1, y) in it.combinations(enumerate(nums), 2):
        if x + y == target:
            break
    return [i0, i1]
