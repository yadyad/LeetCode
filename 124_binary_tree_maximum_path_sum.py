class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None)->int:
        maxSum = -1001


        def dfs(root: TreeNode)->int:
            nonlocal maxSum
            if not root:
                return 0
            if root.left is None and root.right is None:
                return root.val

            l=dfs(root.left)
            r=dfs(root.right)
            total = l+r+root.val
            left = l+root.val
            right = r+root.val
            if root.val>total and root.val>left and root.val>right:
                maxSum = max(maxSum, root.val)
                return root.val
            if total>=left and total>=right:
                maxSum = max(maxSum, total)
                return 0
            if right<=left:
                maxSum = max(maxSum, left)
                return left
            else:
                maxSum = max(maxSum, right)
                return right

        dfs(root)
        return maxSum

s = Solution()
from BuildTree import *
r = build_tree([2,-1,-2])

print(s.maxPathSum(r))




