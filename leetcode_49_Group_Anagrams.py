# coding: utf-8


# def group_anagrams(strs):
#     """
#     Given an array of strings, group anagrams together.
#     :param strs: List[str]
#     :return: List[List[str]]
#     """
#     if not strs:
#         return [[]]
#     strs.sort()
#     n = len(strs)
#
#     ret = []
#     for i in range(n):
#         try:
#             a = [strs[i]]
#             for j in strs[i+1:]:
#                 if ''.join(sorted(j)) == ''.join(sorted(strs[i])):
#                     a.append(j)
#                     strs.remove(j)
#             ret.append(a)
#         except IndexError:
#             break
#
#     return ret
def group_anagrams(strs):
    """
    Given an array of strings, group anagrams together.
    :param strs: List[str]
    :return: List[List[str]]
    """
    letter_dict = {}
    for word in strs:
        key = ''.join(sorted(word))
        letter_dict[key] = letter_dict.get(key, []) + [word]

    return [i for i in letter_dict.values()]


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))