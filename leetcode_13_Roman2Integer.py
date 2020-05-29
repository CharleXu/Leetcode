# coding: utf-8


def roman_to_int(s):
    if not s:
        return
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    roman = list(map(roman_dict.get, [i for i in s]))
    n = len(roman)
    if n == 1:
        return roman[0]
    else:
        ret = 0
        for i in range(len(roman)-1):
            if roman[i] < roman[i+1]:
                ret -= roman[i]
            else:
                ret += roman[i]
        ret += roman[i+1]

    return int(ret)


if __name__ == "__main__":
    l1 = ['IV', 'III', 'IX', 'LVIII', 'D']
    for s in l1:
        print(roman_to_int(s))

