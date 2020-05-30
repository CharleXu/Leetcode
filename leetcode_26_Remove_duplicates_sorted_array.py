# coding: utf-8


def remove_duplicates(nums):
    if not nums:
        return 0
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


if __name__ == "__main__":
    li = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates(li))
