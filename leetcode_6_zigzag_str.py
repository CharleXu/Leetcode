# coding: utf-8


def convert(s, rows):
    if rows == 1:
        return s
    ret = []
    n = len(s)
    cycle = 2 * rows - 2
    for i in range(rows):
        for j in range(0, n - i, cycle):
            ret.append(s[j+i])
            if i != 0 and i != rows - 1 and j + cycle - i < n:
                ret.append(s[j + cycle - i])
    print(ret)
    return "".join(ret)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    num_rows = 4
    print(convert(s, num_rows))
