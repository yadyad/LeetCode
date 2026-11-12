
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkValid(self, root: TreeNode | None,m) -> int:
        if not root:
            return 0
        if root.val == m:
            return 1+self.checkValid(root.left,m)+self.checkValid(root.right,m)
        if root.val > m:
            m = root.val
            return 1+self.checkValid(root.left,m)+self.checkValid(root.right,m)
        return self.checkValid(root.left,m)+self.checkValid(root.right,m)



    def goodNodes(self, root: TreeNode) -> int:
        return self.checkValid(root,root.val)