# coding: utf-8


def four_sum(nums, target):
    """

    :param nums: list[int]
    :param target: int
    :return: list[list[int]]
    """
    if not nums or len(nums) < 4:
        return []
    n = len(nums)
    nums.sort()
    ret = []
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            res = target - nums[i] - nums[j]
            l = j + 1
            r = n - 1
            while l < r:
                curr = nums[l] + nums[r]
                if curr == res and sorted([nums[i], nums[j], nums[l], nums[r]]) not in ret:
                    ret.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                elif curr < res:
                    l += 1
                else:
                    r -= 1

    return ret


if __name__ == "__main__":
    li = [-3,-2,-1,0,0,1,2,3]
    print(four_sum(li, 0))
