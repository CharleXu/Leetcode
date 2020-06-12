# coding:utf-8


def trap(height):
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.
    :param height: List[int]
    :return: int
    """
    if not height:
        return 0

    ans = 0
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    right_max[-1] = height[-1]
    for i in range(1, n):
        left_max[i] = max(height[i], left_max[i - 1])

    for i in range(n - 2, -1, -1):
        right_max[i] = max(height[i], right_max[i + 1])

    for i in range(1, n - 1):
        ans += min(left_max[i], right_max[i]) - height[i]

    return ans


if __name__ == "__main__":
    li = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(li))
