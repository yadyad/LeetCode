#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


def build_tree(values):
    """Build a binary tree from a BFS list; None represents a missing child."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root):
    """Convert a tree to BFS order, trimming trailing missing children."""
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(curr):
            if curr is None:
                return None
            curr.left, curr.right = curr.right, curr.left
            dfs(curr.right)
            dfs(curr.left)

        dfs(root)
        return root


values = [4, 2, 7, 1, 3, 6, 9]
root = build_tree(values)
s = Solution()
inverted_root = s.invertTree(root)
actual = tree_to_list(inverted_root)
expected = [4, 7, 2, 9, 6, 3, 1]

print("Inverted tree:", actual)
assert actual == expected, f"Expected {expected}, got {actual}"
print("Test passed!")