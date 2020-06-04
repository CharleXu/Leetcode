# coding: utf-8


def search_range(nums, target):
    """

    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    if not nums or target not in nums:
        return [-1, -1]
    n = len(nums)
    if n < 2 and target in nums:
        return [0, 0]
    l = 0
    r = n - 1
    ret = []
    while l < r + 1:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            if mid == 0 or nums[mid - 1] != target:
                ret.append(mid)
                break
            else:
                r = mid - 1

    if mid == n - 1 or nums[mid + 1] != target:
        ret.append(mid)
    else:
        while mid + 1 < n and nums[mid + 1] == target:
            mid += 1
        ret.append(mid)

    return ret


if __name__ == "__main__":
    li = [5, 7, 7, 8, 8, 10]
    t = 8
    print(search_range(li, t))
