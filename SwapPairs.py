# Definition for singly-linked list.
#Swap intermediate pairs in a singly linked list
from typing import List,Optional
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        starting = True
        while temp:
            if not temp.next:
                return head
            if starting:
                head = temp.next
                starting = False
            else:
                tempHead.next = temp.next
            tempHead = temp
            temp = temp.next
            tempNext = temp.next
            temp.next = tempHead
            tempHead.next = tempNext
            temp = tempNext
        return head
sol = Solution()
a = sol.swapPairs(sol.asList([1,2,3,4]))
while a:
    print(a.val)
    a = a.next