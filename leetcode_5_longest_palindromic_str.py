# coding: utf-8


def longest_palindrome(s):
    if not s:
        return ""
    n = len(s)
    start, end = 0, 0
    for i in range(n):
        len1 = _expand_around_center(s, i, i)
        len2 = _expand_around_center(s, i, i + 1)
        len3 = max(len1, len2)
        if len3 > end - start:
            start = i - (len3 - 1) // 2
            end = i + len3 // 2
    # print(int(start), int(end+1))
    return s[int(start):int(end + 1)]


def _expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


if __name__ == "__main__":
    s = 'abcdcbaefg'
    print(longest_palindrome(s))