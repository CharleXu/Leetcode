# coding: utf-8
import re


def my_atoi(s):
    s = s.strip()
    nums = re.findall("[\+\-]{0,1}[0-9]+", s)

    if len(nums) == 0:
        return 0
    if not s[0].isnumeric():
        if s[0] not in ['+', '-'] or not s[1].isnumeric():
            return 0

    return min(max(int(nums[0]), -(2 ** 31)), 2 ** 31 - 1)


if __name__ == "__main__":
    l1 = ['+-2', '3.14', '1', ' ', '', '-', '+', 'words and 987', '3.14159', '   -42', '4193 with words',
          '-91283472332']
    for i in l1:
        print(my_atoi(i))
