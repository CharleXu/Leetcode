# coding: utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_node_from_end(head, n):
    """

    :param head: ListNode
    :param n: int
    :return: ListNode
    """
    if not head:
        return
    fake_head = ListNode(0)
    fake_head.next = head
    fast, slow = fake_head, fake_head
    i = 1
    while i <= n + 1:
        fast = fast.next
        i += 1

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return fake_head.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    print(remove_node_from_end(l1, 2))

