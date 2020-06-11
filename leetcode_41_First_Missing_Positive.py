# coding: utf-8


def first_missing_positive(nums):
    """
    Given an unsorted integer array, find the smallest missing positive integer.
    :param nums: List[int]
    :return: int
    """
    if not nums:
        return 1

    for i in range(1, len(nums)+1):
        if i not in nums:
            return i


if __name__ == "__main__":
    n = [3,4,-1,1]
    print(first_missing_positive(n))
