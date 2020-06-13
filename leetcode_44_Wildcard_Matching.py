# coding: utf-8


def is_match(s, p):
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '?' and '*'.
    :param s: str
    :param p: str
    :return: bool
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] in {s[i - 1], '?'}:
                dp[i][j] = dp[i - 1][j - 1]
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[-1][-1]


if __name__ == "__main__":
    d = {"adceb": "*a*b", "acdcb": "a*c?b"}
    for k, v in d.items():
        print(is_match(k, v))
