'''
23. 合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        def merge2(a: ListNode, b: ListNode) -> ListNode:
            if not a:
                return b
            if not b:
                return a
            if a.val< b.val:
                a.next =  merge2(a.next,b)
                return a
            else:
                b.next = merge2(a,b.next)
                return b
        k = len(lists)
        if k == 1:
            return lists[0]
        if k == 0:
            return []
        if k == 2:
            return merge2(lists[0],lists[1])
        mid = k//2
        return merge2(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))
        







