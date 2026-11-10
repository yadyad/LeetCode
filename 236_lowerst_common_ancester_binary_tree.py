
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def combinedict(self, l: dict,r: dict):
        if not l:
            return r
        if not r:
            return l
        if len(l.keys()) < len(r.keys()):
            for key in l.keys():
                if key not in r.keys():
                    r[key] = l[key]
                else:
                    r[key] = r[key].expand(l[key])
            return r
        else:
            for key in r.keys():
                if key not in l.keys():
                    l[key] = r[key]
                else:
                    l[key] = r[key].extend(r[key])
            return l


    def checkLCA(self,root: TreeNode, p,q,depth = 0):
        if root is None:
            return {}
        depth += 1
        l_cand = self.checkLCA(root.left, p, q,depth)
        r_cand = self.checkLCA(root.right, p, q,depth)
        res = self.combinedict(l_cand,r_cand)
        if p.val == root.val:
            if depth in res.keys():
               res[depth].extend(p.val)
            else:
                res[depth]=[p.val]
        if q.val == root.val:
            if depth in res.keys():
                res[depth].extend(q.val)
            else:
                res[depth] = [q.val]
        return res







    def lowestCommonAncestor(self, root: 'TreeNode', p, q):
        return self.checkLCA(root, p, q)

s = Solution()
from BuildTree import *
r = build_tree([3,5,1,6,2,0,8,None,None,7,4])
p = TreeNode(5)
q = TreeNode(4)
print(s.lowestCommonAncestor(r,p,q))

