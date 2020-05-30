# coding: utf-8


def is_valid(s):
    if not s:
        return True
    queue = []
    for i in s:
        if i in ['(', '{', '[']:
            queue.append(i)
        if i in [')', '}', ']'] and queue:
            a = queue.pop()
            ret = ''.join([a, i])
            if ret in ['()', '{}', '[]']:
                continue
            else:
                return False
        if not queue:
            return False

    return False if queue else True


if __name__ == "__main__":
    li = ["", "]", "["]
    for i in li:
        print(is_valid(i))
