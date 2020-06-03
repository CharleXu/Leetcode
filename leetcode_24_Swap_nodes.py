# coding: utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    """

    :param head: ListNode
    :return: ListNode
    """
    if not head:
        return
    dummy = ListNode(0)
    dummy.next = head
    a, b, c = dummy, dummy.next, dummy.next.next
    while a.next:
        if not c:
            break
        a.next = c
        b.next = c.next
        c.next = b
        if not c.next.next:
            break
        a = a.next.next
        b = b.next.next
        c = c.next.next
        b, c = c, b

    return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    print(swap_pairs(l1))
