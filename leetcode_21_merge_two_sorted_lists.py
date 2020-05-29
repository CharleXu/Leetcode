# coding: utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    head = ListNode()
    cur = head
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, cur = l1, l1
            l1 = l1.next
        else:
            cur.next, cur = l2, l2
            l2 = l2.next
    while l1:
        cur.next, cur = l1, l1
        l1 = l1.next
    while l2:
        cur.next, cur = l2, l2
        l2 = l2.next

    return head.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    print(merge_two_lists(l1, l2))


