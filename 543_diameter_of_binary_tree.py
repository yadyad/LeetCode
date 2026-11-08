# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:




    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest = 0

        def countLargestPath(head):
            if not head:
                return 0
            nonlocal largest
            l = countLargestPath(head.left)
            r = countLargestPath(head.right)
            largest = max(largest, l + r)
            return 1 + max(l, r)
        countLargestPath(root)
        return largest

s = Solution()
from BuildTree import *
r = build_tree([1,2,3,4,5])
print(s.diameterOfBinaryTree(r))
