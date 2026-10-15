from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    class Solution:
        def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            temp = head
            while temp:
                newNode = Node(temp.val)
                temp2 = temp.next
                temp.next = newNode
                newNode.next = temp2
                temp = temp2
            temp = head
            while temp:
                temp2 = temp.next
                if temp.random:
                    temp2.random = temp.random.next
                else:
                    temp2.random = None
                temp = temp.next.next
            temp = head
            head2 = temp.next
            while temp:
                temp2 = temp.next
                if not temp.next.next:
                    temp.next = None
                    temp2.next = None
                    break

                temp.next = temp2.next
                temp2.next = temp.next.next
                temp = temp.next
            return head2
