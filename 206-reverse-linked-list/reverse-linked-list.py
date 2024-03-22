# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        iterator = head
        if head!= None:
            while iterator:
                newHead = ListNode(iterator.val,newHead)
                iterator = iterator.next
            return newHead
        else:
            return head