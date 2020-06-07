# coding: utf-8


def max_subarray(nums):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.
    :param nums: List[int]
    :return: int
    """
    if not nums:
        return
    n = len(nums)
    sub = [0] * n

    sub[0] = nums[0]

    for i in range(1, n):
        sub[i] = max(sub[i-1] + nums[i], nums[i])

    return max(sub)


if __name__ == "__main__":
    li = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarray(li))