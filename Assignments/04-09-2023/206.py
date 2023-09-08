class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=None
        while head!=None:
            nxt= head.next
            head.next = ans
            ans = head
            head = nxt
        return ans 