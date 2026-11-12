class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node: TreeNode | None, min_value, max_value) -> bool:
            if not node:
                return True
            if not(min_value < node.val < max_value):
                return False
            return validate(node.left, min_value, node.val) and validate(node.right, node.val, max_value)
        return validate(root,float('-inf'),float('inf'))
