# coding: utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    """
    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    k is a positive integer and is less than or equal to the length of the linked list.
    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
    :param head: ListNode
    :param k: int
    :return: ListNode
    """
    if not head:
        return

    def reverse(a, b):
        curr = a
        prev = None
        while curr != b:
            curr.next, prev, curr = prev, curr, curr.next

        return prev

    a = b = head
    for i in range(k):
        if not b:
            return head
        b = b.next

    rev_head = reverse(a, b)
    a.next = reverse_k_group(b, k)

    return rev_head


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    print(reverse_k_group(a, 3))

    