# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create( nums):
    head = ListNode()
    head.val = nums[0]
    head.next = None
    curr = head
    for i in range(1,len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    return head


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        # Step 1: Find the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None


        printList(second)
        printList(head)
        iter2 = second
        firstTime = True
        head2 = None
        previous = None
        while iter2:
            front = iter2.next
            if not front:
                iter2.next = previous
                head2 = iter2
                break
            if firstTime:
                firstTime = False
                iter2.next = None
            else:
                iter2.next = previous
            previous = iter2
            iter2 = front

        printList(head2)

        iter3 = head
        iter4 = head2
        while iter3 and iter4:
            front1 = iter3.next
            front2 = iter4.next
            iter3.next = iter4
            iter4.next = front1
            iter3 = front1
            iter4 = front2
        printList(head)






def printList(listNode):
    if not listNode:
        print("empty list")
    while listNode:
        print(listNode.val,end=" ")
        listNode = listNode.next
    print("\n")

s = Solution()
ll = create([1,2,3,4,5,6,7,8,9,10,11])
curr = ll
print(f"reorder {s.reorderList(ll)}")