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

        ans = []
        s = deque([root])
        while s:
            top = s.pop()
            ans.append(top.val)
            if top.right is not None:
                s.append(top.right)
            if top.left is not None:
                s.append(top.left)

        return ans


if __name__ == "__main__":
    # root = TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
    # root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    print(repr(Solution().inorderTraversal(root)))

    pass
