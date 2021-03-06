# coding: utf-8


def is_match(s, p):
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
    :param s: str
    :param p: str
    :return: bool
    """
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            first_match = i < len(s) and p[j] in {s[i], '.'}
            if j + 1 < len(p) and p[j + 1] == '*':
                dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
            else:
                dp[i][j] = first_match and dp[i+1][j+1]

    return dp[0][0]


if __name__ == "__main__":
    s = "mississippi"
    p = "mis*is*p*."
    print(is_match(s, p))