# coding: utf-8


def permute_unique(nums):
    """

    :param nums: List[int]
    :return: List[List[int]]
    """

    def _helper(n):
        if len(n) == 1:
            return [[n[0]]]

        ret = []
        visited = []
        for j in range(len(n)):
            if n[j] in visited:
                continue
            n_copy = n.copy()
            n_copy.remove(n[j])
            res = _helper(n_copy)
            perm = [[n[j]] + i for i in res]
            ret.extend(perm)
            visited.append(n[j])

        return ret

    return _helper(nums)


if __name__ == "__main__":
    li = [1, 1, 3]
    print(permute_unique(li))

