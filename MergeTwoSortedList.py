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


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head = ListNode()
        temp = head
        while(list1!=None or list2!=None):
            if(list1.val==list2.val):
                temp.next = list1
                temp = temp.next
                list1 = list1.next
                temp.next = list2
                temp = temp.next
                list2 = list2.next
            elif(list1.val > list2.val):
                temp.next = list2
                temp = temp.next
                list2 = list2.next
            else:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
        if list1 or list2:
            temp.next = list1 if list1 else list2
        return head
sol = Solution()
head = sol.mergeTwoLists(sol.asList([1,2,4]),sol.asList([1,3,4]))
head = head.next
while(head.next!=None):
    print(head.val)
    head = head.next



