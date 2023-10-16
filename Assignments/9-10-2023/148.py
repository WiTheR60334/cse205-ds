# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(head):
            slow=fast=head
            while fast.next and fast.next.next:
                slow,fast=slow.next,fast.next.next
            return slow
        
        def merge(left,right):
            temp=ListNode()
            curr=temp
            while left and right:
                if right.val>left.val:
                    curr.next,left=left,left.next
                else:
                    curr.next,right=right,right.next
                curr=curr.next
            curr.next=left or right
            return temp.next
        
        def sort(head):
            if not head or not head.next:
                return head
            mid=middle(head)
            left,right=head,mid.next
            mid.next=None
            left=sort(left)
            right=sort(right)
            return merge(left,right)
            
        return sort(head)