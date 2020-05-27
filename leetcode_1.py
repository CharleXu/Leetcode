# coding: utf-8


def twoSum(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in num_dict:
            return [num_dict[res], i]
        num_dict[nums[i]] = i
    return []


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))