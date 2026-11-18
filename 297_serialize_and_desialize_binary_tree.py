from collections import deque

from CombinationSum2 import Solution


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        res = []
        queue = deque([root])
        while queue:
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.popleft()
                if node is None:
                    res.append("null")
                    continue
                else:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
        result = ','.join([str(s) for s in res])
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        string_list = data.split(',')
        tree_string = deque(string_list)
        root = TreeNode(int(tree_string.popleft()))
        stack_tree = deque([root])
        while tree_string:
            len_stack = len(stack_tree)
            for i in range(len_stack):
                node = stack_tree.popleft()
                if node is None:
                    continue
                left_node = tree_string.popleft()
                right_node = tree_string.popleft()


                if left_node=="null":
                    node.left = None

                else:
                    node.left = TreeNode(int(left_node))
                if right_node=="null":
                    node.right = None
                else:
                    node.right = TreeNode(int(right_node))


                if node.left:
                    stack_tree.append(node.left)
                if node.right:
                    stack_tree.append(node.right)

        return root




ser = Codec()
deser = Codec()
from BuildTree import *
r = build_tree([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2])
s = ser.serialize(r)
d = deser.deserialize(s)
print(tree_to_list(d))


