# coding: utf-8
from itertools import permutations


def next_permutation(nums):
    """

    :param nums: List[int]
    :return: None
    """
    if not nums:
        return
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1
    if i >= 0:
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    k = n - 1
    while i + 1 < k:
        nums[i + 1], nums[k] = nums[k], nums[i + 1]
        i += 1
        j -= 1


if __name__ == "__main__":
    nums = [1, 2, 3]
    next_permutation(nums)
    print(nums)
