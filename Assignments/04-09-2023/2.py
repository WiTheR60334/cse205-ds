class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev1=rev2=None
        while l1:
            nxt=l1.next
            l1.next=rev1
            rev1=l1
            l1=nxt
        while l2:
            nxt=l2.next
            l2.next=rev2
            rev2=l2
            l2=nxt 
        r1=r2=0
        while rev1:
            r1=r1*10+rev1.val
            rev1=rev1.next
        while rev2:
            r2=r2*10+rev2.val
            rev2=rev2.next
        sum=r1+r2
        inttostr=(str(sum)[::-1])
        head=curr=None
        for i in inttostr:
            new=ListNode(int(i))
            if not head:
                head=new
                curr=head
            else:
                curr.next=new
                curr=new
        return head