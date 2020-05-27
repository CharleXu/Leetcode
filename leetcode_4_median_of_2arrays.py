# coding: utf-8


def merge(left, right):
    """合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组"""
    # left与right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def find_median_sorted_arrays(nums1, nums2):
    if not (nums1 or nums2):
        return None
    new = merge(nums1, nums2)
    n = len(new)

    if n % 2 != 0:
        return float(new[n // 2])
    else:
        return .5 * (new[int(n / 2)] + new[int(n / 2 - 1)])


nums1 = [1, 2]
nums2 = [3, 4]
print(find_median_sorted_arrays(nums1, nums2))