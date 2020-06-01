# coding: utf-8


def three_sum(nums):
    if not nums or len(nums) < 3:
        return []
    nums.sort()
    ret = []
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            res = nums[i] + nums[l] + nums[r]
            if res == 0:
                ret.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif res < 0:
                l += 1
            else:
                r -= 1
    return ret


if __name__ == "__main__":
    li = [[-1, 0, 1, 2, -1, -4], [1, 2], [1, 2, -2, -1]]
    for l in li:
        print(three_sum(l))