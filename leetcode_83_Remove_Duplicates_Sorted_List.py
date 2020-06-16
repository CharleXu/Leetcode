# coding: utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    """
    Given a sorted linked list, delete all duplicates such that each element appear only once.
    :param head: ListNode
    :return: ListNode
    """
    if not head:
        return

    prev, cur = head, head.next

    while cur:
        if cur.val == prev.val:
            cur = cur.next
            prev.next = cur
        else:
            cur, prev = cur.next, prev.next

    return head


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(1)
    l3 = ListNode(2)
    l4 = ListNode(3)
    l5 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    print(delete_duplicates(l1))
