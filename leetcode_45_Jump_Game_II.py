# coding: utf-8


def jump(nums):
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Your goal is to reach the last index in the minimum number of jumps.
    :param nums: List[int]
    :return: int
    """
    if not nums:
        return

    n = len(nums)
    if n == 1:
        return 0

    cur, max_pos, jumps = nums[0], nums[0], 1
    for i in range(n):
        if i > cur:
            jumps += 1
            cur = max_pos
        max_pos = max(max_pos, nums[i] + i)

    return jumps


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))


