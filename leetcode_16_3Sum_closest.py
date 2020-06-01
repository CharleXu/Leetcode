# coding: utf-8


def three_sum_closest(nums, target):
    """

    :param nums: list[int]
    :param target: int
    :return: int
    """
    if not nums or len(nums) < 3:
        return
    diff = float('inf')
    n = len(nums)
    nums.sort()
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            ret = nums[i] + nums[l] + nums[r]
            if abs(target - ret) < abs(diff):
                diff = target - ret
            if ret < target:
                l += 1
            else:
                r -= 1
        if diff == 0:
            break
    return target - diff


if __name__ == "__main__":
    li = [-1, 2, 1, -4]
    print(three_sum_closest(li, 1))
