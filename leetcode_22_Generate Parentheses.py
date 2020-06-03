# coding: utf-8


# def generate_parenthesis(n):
#     """
#
#     :param n: int
#     :return: List[str]
#     """
#     if n == 0:
#         return ['']
#     ans = []
#     for i in range(n):
#         for l in generate_parenthesis(i):
#             for r in generate_parenthesis(n-1-i):
#                 ans.append(f'({l}){r}')
#
#     return ans


def generate_parenthesis(n):
    ans = []

    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            ans.append(s)
            return
        if left < n:
            backtrack(s+'(', left+1, right)
        if right < left:
            backtrack(s+')', left, right+1)

    backtrack()

    return ans


if __name__ == "__main__":
    n = 3
    print(generate_parenthesis(n))