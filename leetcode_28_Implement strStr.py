# coding: utf-8


def strStr(haystack, needle):
    if not needle:
        return 0
    # if not haystack:
    #     return -1
    return haystack.find(needle)


if __name__ == "__main__":
    h = ''
    n = ''
    print(strStr(h, n))
