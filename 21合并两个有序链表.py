class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def mergeTwoLists(self, a: ListNode, b: ListNode) -> ListNode:
        c = ListNode(None)
        f = ListNode(None)
        f.next = c
        while a and b:
            if a.val < b.val:
                c.next = a
                a = a.next
            else:
                c.next = b
                b = b.next
            c = c.next
        if not a:
            
            c.next = b
        if not b:
            
            c.next = a
        return f.next.next
#递归
class Solution2:
    def mergeTwoLists(self, a: ListNode, b: ListNode) -> ListNode:
        if not a:
            return b
        if not b:
            return a
        if a.val< b.val:
            a.next =  self.mergeTwoLists(a.next,b)
            return a
        else:
            b.next = self.mergeTwoLists(a,b.next)
            return b