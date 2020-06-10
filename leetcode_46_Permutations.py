# coding: utf-8


# def permute(nums):
#     """
#
#     :param nums: List[int]
#     :return: List[List[int]]
#     """
#
#     def _helper(n):
#         if len(n) == 1:
#             return [[n[0]]]
#
#         ret = []
#         for j in range(len(n)):
#             n_copy = n.copy()
#             n_copy.remove(n[j])
#             res = _helper(n_copy)
#             perm = [[n[j]] + i for i in res]
#             ret.extend(perm)
#
#         return ret
#
#     return _helper(nums)


def permute(nums):
    """

    :param nums: List[int]
    :return: List[List[int]]
    """
    ret = []

    def _helper(nums, p, q):
        if p == q:
            ret.append(nums)
        else:
            for i in range(p, q+1):
                nums[i], nums[p] = nums[p], nums[i]
                _helper(nums, p+1, q)
                nums[i], nums[p] = nums[p], nums[i]

    _helper(nums, 0, len(nums)-1)
    return ret


if __name__ == "__main__":
    li = [1, 2, 3, 4]
    print(permute(li))

