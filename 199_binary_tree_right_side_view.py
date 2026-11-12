from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        queue = deque()
        if not root:
            return []
        queue.append(root)
        flag=True
        result=[]
        while queue:
            len_queue = len(queue)
            for _ in range(len_queue):
                node = queue.popleft()
                if flag:
                    result.append(node.val)
                    flag=False
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            flag=True
        return result

s = Solution()
from BuildTree import *
r=build_tree([1,2,3,4,None,None,None,5])
print(s.rightSideView(r))

