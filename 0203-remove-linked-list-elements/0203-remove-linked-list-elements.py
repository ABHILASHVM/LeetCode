# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        start=ListNode(0,head)
        prev=start
        curr=head
        # head.next
        while curr:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
            
        return start.next