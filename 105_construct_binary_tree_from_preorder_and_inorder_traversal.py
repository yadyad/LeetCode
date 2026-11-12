# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def extract_in_order(self,list1, list2):
        """
        Returns elements from list2 that are present in list1, preserving list2's order.
        Handles duplicates and ignores elements not in list1.
        """
        # Convert list1 to a set for faster lookup
        lookup = set(list1)

        # Filter list2 based on presence in list1
        return [item for item in list2 if item in lookup]
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        pos_root_inorder = inorder.index(preorder[0])
        root.left = self.buildTree(self.extract_in_order(inorder[0:pos_root_inorder],preorder),inorder[0:pos_root_inorder])
        root.right = self.buildTree(self.extract_in_order(inorder[pos_root_inorder+1:],preorder),inorder[pos_root_inorder+1:])
        return root

class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mapping = {}

        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        preorder = collections.deque(preorder)

        def build(start, end):
            if start > end: return None

            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)

s = Solution()
root = s.buildTree([3,9,20,15,7],[9,3,15,20,7])
from BuildTree import *
print(tree_to_list(root))