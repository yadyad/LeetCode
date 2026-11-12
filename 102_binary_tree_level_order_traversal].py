from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            level = []
            len_level = len(queue)
            for _ in range(len_level):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


s = Solution()
from BuildTree import *
root = build_tree([3,9,20,None,None,15,7])
print(s.levelOrder(root))


