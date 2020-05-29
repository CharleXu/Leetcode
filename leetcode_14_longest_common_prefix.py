# coding: utf-8


def longest_common_prefix(strs):
    if not strs:
        return ""
    n = len(strs)
    prefix = strs[0]
    for i in range(1, n):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0:len(prefix) - 1]
            if not prefix:
                return ""

    return prefix


if __name__ == "__main__":
    li = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
    for l in li:
        print(longest_common_prefix(l))