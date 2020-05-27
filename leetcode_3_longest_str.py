# coding: utf-8


def length_of_longest_substring(s):
    if not s:
        return 0
    n = len(s)
    sub_str = dict()
    ans = 0
    i = 0
    for j in range(n):
        if s[j] in sub_str.keys():
            i = max(sub_str[s[j]], i)
        ans = max(ans, j - i + 1)
        sub_str[s[j]] = j + 1

    return ans


s = 'pwwkew'
print(length_of_longest_substring(s))