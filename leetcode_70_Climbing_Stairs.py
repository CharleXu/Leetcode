# coding: utf-8


def climb_stairs(n):
    """
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    :param n: int
    :return: int
    """
    ret = {0: 0, 1: 1, 2: 2}
    for i in range(3, n+1):
        ret[i] = ret[i-1] + ret[i-2]
    return ret[n]


if __name__ == "__main__":
    n = 3
    print(climb_stairs(n))