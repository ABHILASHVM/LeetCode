# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dum=ListNode(0)
        curr=dum
        save=head
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        if save:
            lst=lst[-(k%len(lst)):]+lst[:-(k%len(lst))]
        for i in lst:
            dum.next=ListNode(i)
            dum=dum.next
        return curr.next