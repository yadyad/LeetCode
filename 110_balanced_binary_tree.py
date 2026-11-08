# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isBalanced(self, root: TreeNode | None) -> bool:
        res = True

        def getlongestPathDown(root: TreeNode) -> int:
            if root is None:
                return 0
            left = getlongestPathDown(root.left)
            right = getlongestPathDown(root.right)
            nonlocal res
            if abs(left - right) > 1:
                res = False
            return max(left, right) + 1
        getlongestPathDown(root)
        return res

s = Solution()
from BuildTree import *
r=build_tree([1,2,2,3,3,None,None,4,4])
print(s.isBalanced(r))