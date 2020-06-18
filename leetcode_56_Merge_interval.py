# coding: utf-8


def merge(intervals):
    """
    Given a collection of intervals, merge all overlapping intervals.
    :param intervals: List[List[int]]
    :return: List[List[int]]
    """
    intervals.sort(key=lambda x: x[0])

    ret = []
    for i in intervals:
        if not ret or ret[-1][1] < i[0]:
            ret.append(i)
        else:
            ret[-1][1] = max(ret[-1][1], i[1])

    return ret


if __name__ == "__main__":
    li = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(li))