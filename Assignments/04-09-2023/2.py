class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev1,rev2=None,None
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

        r1 = 0
        while rev1:
            r1 = r1 * 10 + rev1.val
            rev1 = rev1.next
        r2 = 0
        while rev2:
            r2 = r2 * 10 + rev2.val
            rev2 = rev2.next
        sum=r1+r2
        numtostr=(str(sum)[::-1])
        head,curr=None,None
        for i in numtostr:
            new=ListNode(int(i))
            if not head:
                head=new
                current=head  
            else:    
                current.next=new
                current=new
        return(head)