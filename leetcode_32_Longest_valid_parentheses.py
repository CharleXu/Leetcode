# coding: utf-8


def longest_valid_parentheses(s):
    max_len = 0
    stack = [-1]
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


if __name__ == "__main__":
    li = ")()())"
    print(longest_valid_parentheses(li))
