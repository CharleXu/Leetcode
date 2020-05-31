# coding: utf-8


def max_area(height):
    """

    :param height: list[int]
    :return: int
    """
    max_ = 0
    l = 0
    r = len(height) - 1
    while l < r:
        max_ = max(max_, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_


if __name__ == "__main__":
    h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(h))