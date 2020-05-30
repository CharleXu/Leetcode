# coding: utf-8


def remove_elements(nums, val):
    if not nums:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i


if __name__ == "__main__":
    li = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_elements(li, 2))
