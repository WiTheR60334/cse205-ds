class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode()
        cur = head
        while cur:
            temp = sort
            while temp.next and cur.val >= temp.next.val:
                temp = temp.next
            temp1, temp.next = temp.next, cur
            cur = cur.next
            temp.next.next = temp1
        return sort.next