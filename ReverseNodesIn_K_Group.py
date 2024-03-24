# Definition for singly-linked list.
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        print("ReverseKGroup")
        temp = head
        flag = True
        prev1 = None
        while(temp):
            curHead = temp
            for i in range(k-1):
                if temp.next is not None:
                    temp = temp.next
                else:
                    return mainHead
            curEnd = temp.next
            temp.next = None
            headRev = self.reverseAndAdd(curHead,curEnd)
            if(prev1):
                prev1.next = headRev
            if(flag):
                mainHead = temp
                flag = False
            prev1 = curHead
            temp = curEnd
        return mainHead
    def reverseAndAdd(self,headRev : Optional[ListNode],tail : Optional[ListNode]):
        temp1 = headRev
        prev = tail
        current = headRev
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        headRev = prev
        return headRev
    def reverseKGroupOptim(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Step 1
        # Reverse K nodes
        # Step 2
        # Recursively call function to reverse K nodes
        # step 3 attach each of the k nodes that are reversed
        cur = head
        for i in range(k):
            if not cur:
                return head
            cur = cur.next
        prevNode = None
        curNode = head
        tail = head
        for i in range(k):
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        
        head = prevNode
        curNode = self.reverseKGroup(curNode, k)
        tail.next = curNode
        return head
sol = Solution()

a = sol.reverseKGroup(sol.asList([1,2,3,4,5]),3)
while a:
    print(a.val)
    a = a.next



                
                
                    


