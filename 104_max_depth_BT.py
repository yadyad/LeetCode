
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def dfs(curr,depth):
            if curr is None:
                return 0
            l_depth = dfs(curr.left,depth)
            r_depth = dfs(curr.right,depth)
            depth = 1+max(l_depth,r_depth)
            return depth
        return dfs(root,0)