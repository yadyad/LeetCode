# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = 0
        count = 0
        def inorder(root, k_in):
            if not root:
                return
            nonlocal res
            nonlocal count
            inorder(root.left, k_in)
            count = count + 1
            if count == k_in:
                res = root.val
            inorder(root.right, k_in)

        if not root.left and not root.right:
            return root.val
        inorder(root, k)
        return res
s = Solution()
from BuildTree import *
r = build_tree([3,1,4,None,2])
print(s.kthSmallest(r,3))