class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goThroughTwoTree(self, p: TreeNode, q: TreeNode)-> False:
        if p is None and q is None:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val != q.val:
            return False
        resl = self.goThroughTwoTree(p.left, q.left)
        resr = self.goThroughTwoTree(p.right, q.right)
        if resl and resr:
            return True
        else:
            return False

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return self.goThroughTwoTree(p, q)

    def findRootNode(self, root: TreeNode | None,subroot) -> bool:
        res = False
        if root.val == subroot.val:
            res = self.isSameTree(root, subroot)
            if res:
                return True
        resl = self.findRootNode(root.left, subroot)
        resr = self.findRootNode(root.right, subroot)
        if resl or resr:
            return True
        else:
            return False
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        return self.findRootNode(root, subRoot)

s=Solution()
from BuildTree import *
r = build_tree([3,4,5,1,2,None,None,None,None,0])
sub = build_tree([4,1,2])
print(s.isSameTree(r,sub))
