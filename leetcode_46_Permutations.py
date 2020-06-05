# coding: utf-8


def permute(nums):
    """

    :param nums: List[int]
    :return: List[List[int]]
    """

    def _helper(n):
        if len(n) == 1:
            return [[n[0]]]

        ret = []
        for j in range(len(n)):
            n_copy = n.copy()
            n_copy.remove(n[j])
            res = _helper(n_copy)
            perm = [[n[j]] + i for i in res]
            ret.extend(perm)

        return ret

    return _helper(nums)


if __name__ == "__main__":
    li = [1, 2, 3]
    print(permute(li))

