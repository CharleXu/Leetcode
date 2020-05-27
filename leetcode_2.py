# coding: utf-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_number(l1, l2):
    result_node = ListNode(0)
    curr = result_node
    carry = 0
    p, q = l1, l2
    while l1 or l2 or carry:
        x = (l1.val if l1 else 0)
        y = (l2.val if l2 else 0)

        total = x + y + carry
        carry = total // 10
        new_val = total % 10

        curr.next = ListNode(new_val)
        curr = curr.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result_node.next


if __name__ == "__main__":
    l1 = ListNode(0)
    l2 = ListNode(0)
    l1.next = ListNode(1)
    # l1.next.next = ListNode(3)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)
    ret = add_two_number(l1, l2)
    while ret.next:
        print(ret.val, end=" -> ")
        ret = ret.next
    print(ret.val)
