# coding: utf-8


def is_palindrome(x):
    s = [i for i in str(x)]
    n = len(s)
    if n == 1:
        return True
    for i in range(n // 2):
        s[i], s[n-i-1] = s[n-i-1], s[i]
    return True if ''.join(s) == str(x) else False


def is_palindrome2(x):
    if x < 0:
        return False
    if 0 <= x < 10:
        return True
    rev, s = 0, x
    while x:
        x, mod = divmod(x, 10)
        rev = rev * 10 + mod

    return rev == s


if __name__ == "__main__":
    l1 = [121, -121, 10, 11]
    for i in l1:
        print(is_palindrome2(i))