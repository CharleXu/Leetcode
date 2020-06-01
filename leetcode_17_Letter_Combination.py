# coding: utf-8


def letter_combine(digits):
    """

    :param digits: str
    :return: list[str]
    """
    phone = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
             6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    ret = []

    def combine(output, digit_):
        if len(digit_) == 0:
            ret.append(output)
        else:
            for s in phone[int(digit_[0])]:
                combine(output+s, digit_[1:])

    if digits:
        combine('', digits)

    return ret


if __name__ == "__main__":
    li = '23'
    print(letter_combine(li))