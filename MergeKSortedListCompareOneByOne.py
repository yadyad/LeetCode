# Definition for singly-linked list.
from dataclasses import dataclass
from queue import Empty, PriorityQueue
from typing import Optional
from typing import List
from typing import Any
from dataclasses import dataclass,field

#Priority Queue sometimes wont allow comparoson
#So we are specifying which element to compare
@dataclass(order=True)
class ListNode:
    val:int
    next:Any=field(compare=False)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def asList(self,array: List):
        head = ListNode()
        temp = head
        temp.val = array[0]
        for i in array[1:]:
            next = ListNode()
            next.val = i
            temp.next = next
            temp = temp.next
        return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print("MergeKLists")
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next







            


        
        

    
sol = Solution()
a = sol.mergeKLists([sol.asList([1,4,5]),sol.asList([3,4,5])])
while a:
    print(a.val)
    a = a.next