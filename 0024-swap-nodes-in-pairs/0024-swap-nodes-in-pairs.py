# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        headi=head
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        # print(lst)
        i=0
        while i < len(lst)-1:
            lst[i],lst[i+1]=lst[i+1],lst[i]
            i+=2
        for i in lst:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return curr.next
        # print(lst)
            # print(head.val)
            # curr.next=headi.next
            # curr.next.next=headi
            # curr=curr.next.next
            # head=headi.next.next
            # print(head.next.val)
     