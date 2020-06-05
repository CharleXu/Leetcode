# coding: utf-8


def combination_sum2(candidates, target):
    """

    :param candidates: List[int] -> [2,3,6,7]
    :param target: int -> 7
    :return: List[List[int]] -> [[7],[2,2,3]]
    """
    if not candidates:
        return []

    def _helper(nums, c, t, index):
        if t > 0:
            i = index
            while i < len(c) and t >= c[i]:
                nums.append(c[i])
                _helper(nums, c, t - c[i], i + 1)
                nums.pop()
                i += 1
        else:
            if t == 0 and nums not in ret:
                ret.append(nums.copy())

    candidates.sort()
    ret = []
    _helper([], candidates, target, 0)

    return ret


if __name__ == "__main__":
    li = [10, 1, 2, 7, 6, 1, 5]
    aim = 8
    print(combination_sum2(li, aim))
