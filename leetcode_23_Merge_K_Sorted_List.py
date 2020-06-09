# coding: utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    """

    :param lists: List[ListNode]
    :return: ListNode
    """

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
    n = len(lists)
    m = 1
    while m < n:
        for i in range(0, n - m, m * 2):
            lists[i] = merge_two_lists(lists[i], lists[i+m])
        m *= 2
    return lists[0] if n > 0 else lists

