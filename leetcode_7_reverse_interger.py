# coding: utf-8


def reverse(x):
    s = [i for i in str(x)]
    if s[0].isdigit():
        s.insert(0, '+')
    n = len(s)
    for i in range(0, n//2):
        s[i+1], s[n-i-1] = s[n-i-1], s[i+1]
    ret = int(''.join(s[1:])) if s[0] == 0 else int(''.join(s))
    return ret if -2 ** 31 <= ret <= 2 ** 31 - 1 else 0


if __name__ == "__main__":
    num = 1534236469
    print(reverse(num))
