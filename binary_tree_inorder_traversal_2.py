from collections import deque
from typing import Optional, List


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.vl = False
        self.vr = False

    def __str__(self):
        return str(self.val)


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        q = deque([root])
        while q:
            top = q[-1]
            if not top.vl:
                top.vl = True
                if top.left is not None:
                    q.append(top.left)
                    continue
            if not top.vr:
                ans.append(top.val)
                top.vr = True
                if top.right is not None:
                    q.append(top.right)
                    continue
            q.pop()

        return ans


if __name__ == "__main__":
    # root = TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3)))
    root = TreeNode(3, left=TreeNode(1, right=TreeNode(2)))
    # root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    print(repr(Solution().inorderTraversal(root)))

    pass
