from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse(head:Optional[ListNode],tail):
    temp = head
    head = head.next
    prev = tail
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    temp.next = head
    return head
def asList(array: List):
        head = ListNode()
        temp = head
        temp.val = 0
        for i in array:
            next = ListNode()
            next.val = i
            temp.next = next
            temp = temp.next
        return head
tail = ListNode(6,None)
a = reverse(asList([1,2,3,4,5]),tail)
while a:
    print(a.val)
    a = a.next
