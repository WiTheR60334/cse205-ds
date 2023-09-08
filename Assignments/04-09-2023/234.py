class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp1,temp2 = head,head

        while temp2 and temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next.next

        prev = None
        while temp1:
            nxt = temp1.next
            temp1.next = prev
            prev = temp1
            temp1 = nxt

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True