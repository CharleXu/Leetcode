# coding: utf-8


def search(nums, target):
    """

    :param nums: List[int]
    :param target: int
    :return: int
    """
    if not nums or target not in nums:
        return -1
    num_dict = {x: i for i, x in enumerate(nums)}
    nums.sort()
    n = len(nums)
    l = 0
    r = n - 1
    while l < r + 1:
        mid = (l + r) // 2
        if nums[mid] == target:
            return num_dict[target]
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1


if __name__ == "__main__":
    li = [4, 5, 6, 7, 0, 1, 2]
    t = 0
    print(search(li, t))