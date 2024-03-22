# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        length = 0
        iterator = head
        # interestedIndex = -1
        count = 0
        iterator2 = head
        
        while iterator:
            length+=1
            iterator = iterator.next

        interestedIndex = length//2

        
        while iterator2:
            if head.next == None:
                head = None
            elif count == interestedIndex-1:
                iterator2.next = iterator2.next.next
                break
            count+=1
            iterator2 = iterator2.next
            

        return head