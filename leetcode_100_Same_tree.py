# coding: utf-8


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    """
    Given two binary trees, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

    :param p: TreeNode
    :param q: TreeNode
    :return: bool
    """
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return is_same_tree(p.right, q.right) and is_same_tree(p.left, q.left)


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    p = q = a
    print(is_same_tree(p, q))

