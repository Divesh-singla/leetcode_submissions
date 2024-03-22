# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # oddData = []
        # evenData = []
        # iterator1 = head
        # newHead = None
        # count = 0
        # while iterator1:
        #     try:
        #         if count%2!=0:
        #             evenData.append(iterator1.val)
        #         else:
        #             oddData.append(iterator1.val)
                
        #     except:
        #         pass
        #     iterator1 = iterator1.next
        #     count+=1
        # for x in evenData[::-1]:
        #     newHead = ListNode(x,newHead)
        # for y in oddData[::-1]:
        #     newHead = ListNode(y,newHead)
        # return newHead

        if head is None:
            return None

        oddHead = head
        result = evenHead = head.next
    
        while evenHead and evenHead.next:
            oddHead.next = oddHead.next.next
            evenHead.next = evenHead.next.next
            oddHead = oddHead.next
            evenHead = evenHead.next


        oddHead.next = result
        return head


            
            