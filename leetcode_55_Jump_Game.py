# coding: utf-8


def can_jump(nums):
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.
    :param nums: List[int]
    :return: bool
    """
    n = len(nums)
    last = n - 1
    for i in range(n - 1, -1, -1):
        if i + nums[i] >= last:
            last = i

    return last == 0


if __name__ == "__main__":
    li = [[2, 3, 1, 1, 4], [3, 2, 1, 0, 4]]
    for i in li:
        print(can_jump(i))
