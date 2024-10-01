# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lsta=['a']
        lstb=['b']
        
        
        while headA or headB:
            if headA:
                lsta.append(headA)
                headA=headA.next
            if headB:
                lstb.append(headB)
                headB=headB.next
        # for i in range(1,len(lsta)):
        #     if lsta[len(lsta)-i] != lstb[len(lstb)-i]:
        #         return lsta[len(lsta)-i+1]
        prev=None
        while lsta and lstb:
            nodea=lsta.pop()
            nodeb=lstb.pop()
            if nodea!=nodeb:
                return prev
            prev=nodea