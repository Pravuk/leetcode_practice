from collections import deque
from typing import Optional, List


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        def stack_lefts(node: TreeNode, stack: deque):
            while node is not None:
                stack.append(node)
                node = node.left

        ans = []
        s = deque()
        stack_lefts(root, s)
        last = TreeNode()
        while s:
            top = s[-1]
            if top.right is not None and top.right != last:
                stack_lefts(top.right, s)
                continue
            ans.append(top.val)
            last = s.pop()

        return ans


if __name__ == "__main__":
    # root = TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
    # root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    print(repr(Solution().inorderTraversal(root)))

    pass
