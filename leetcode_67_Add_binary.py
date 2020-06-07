# coding: utf-8


def add_binary(a, b):
    """
    Given two binary strings, return their sum (also a binary string)
    :param a: str
    :param b: str
    :return: str
    """
    try:
        a = int(a, 2)
        b = int(b, 2)
        return str(bin(a+b))[2:]
    except ValueError:
        return


if __name__ == "__main__":
    a = '11'
    b = '1'
    print(add_binary(a, b))