# coding: utf-8


def int_to_roman(num):
    roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                  'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    ret = ''
    for k, v in roman_dict.items():
        if v > num:
            continue
        else:
            n, num = divmod(num, v)
            ans = n * k
            ret += ans
    return ret


if __name__ == "__main__":
    l1 = [3, 4, 9, 58, 10, 1994]
    for i in l1:
        print(int_to_roman(i))
