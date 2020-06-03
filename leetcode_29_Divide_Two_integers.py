# coding: utf-8


def divide(dividend, divisor):
    """

    :param dividend: int
    :param divisor: int
    :return: int
    """
    ret = int(dividend / divisor)
    if -2 ** 31 <= ret <= 2 ** 31 - 1:
        return ret

    return -2 ** 31 if ret < -2 ** 31 else 2 ** 31 - 1


