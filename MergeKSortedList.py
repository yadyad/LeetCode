# Definition for singly-linked list.
from typing import Optional
from typing import List
class ListNode:
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
        a = []
        count = 0
        for i in lists:
            while i:
                a.append(i.val)
                i = i.next
        a.sort()
        head = ListNode()
        head.val = a[0]
        pointer = head
        for i in a[1:]:
            temp = ListNode()
            temp.val = i
            pointer.next = temp
            pointer = pointer.next
        return head

    
sol = Solution()
a = sol.mergeKLists([sol.asList([1,4,5]),sol.asList([3,4,5])])
while a:
    print(a.val)
    a = a.next
