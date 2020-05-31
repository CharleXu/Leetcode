# coding: utf-8


def search_insert(nums, target):
    """
    :param nums: list[int]
    :param target: int
    :return: int
    """
    n = len(nums)
    if target in nums:
        return nums.index(target)
    else:
        if target > max(nums):
            return n
        elif target < min(nums):
            return 0
        else:
            for i in range(n - 1):
                if nums[i] < target < nums[i + 1]:
                    return i + 1


if __name__ == "__main__":
    li = [1, 3, 5, 6]
    t = 7
    print(search_insert(li, t))
