# coding: utf-8


def subarray_sum(nums, k):
    """
    Given an array of integers and an integer k,

    you need to find the total number of continuous subarrays whose sum equals to k.

    :param nums: List[int]
    :param k: int
    :return: int
    """
    count, total = 0, 0
    res = {0: 1}
    for i in range(len(nums)):
        total += nums[i]
        if total - k in res.keys():
            count += res[total - k]
        res[total] = res.get(total, 0) + 1

    return count


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(subarray_sum(nums, k))

