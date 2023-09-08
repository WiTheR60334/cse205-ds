class Solution:    
    def reverseKGroup(self, head, k):
        def length(head):
            size,temp = 0,head
            while temp:
                temp = temp.next
                size += 1
            return size

        def solve(head, k, size):
            if size < k:
                return head
            if head==None:
                return None
            curr,count = head,0
            nxt = prev = None
            while curr!=None and count < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count += 1
            head.next = solve(nxt, k, size - k)
            return prev
       
        n = length(head)
        return solve(head, k, n)
