# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0)
        s1=""
        s2=""
        tail=dum
        while l1 or l2:
            if l1:
                s1+=str(l1.val)
                l1=l1.next
            if l2:
                s2+=str(l2.val)
                l2=l2.next
        num=int(s1[::-1])+int(s2[::-1])
        num=str(num)[::-1]
        for i in num:
            newnode=ListNode(int(i))
            tail.next=newnode
            tail=tail.next
        return dum.next