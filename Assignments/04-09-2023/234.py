class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        rev=None
        while slow:
            nxt=slow.next
            slow.next=rev
            rev=slow
            slow=nxt
        while rev:
            if rev.val!=head.val:
                return False
            rev=rev.next
            head=head.next
        return True 