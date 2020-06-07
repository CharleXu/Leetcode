# coding: utf-8


def two_sum(nums, target):
    """
    Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
    :param numbers: List[int]
    :param target: int
    :return: List[int]
    """
    num_dict = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in num_dict:
            return sorted([num_dict[res] + 1, i + 1])
            break
        num_dict[nums[i]] = i
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))