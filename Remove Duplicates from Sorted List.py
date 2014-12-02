#Remove Duplicates from Sorted List
#问题描述
#Given a sorted linked list, delete all duplicates such that each element appear only once.
#要求结构单向链表,过滤重复元素
#思路:遍历读到set结构,排序后输出
#点:链表遍历,set默认是无序的


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        pointer=head
        sets=set([])
        while pointer is not None:
            sets.add(pointer.val)
            pointer = pointer.next
        sets=sorted(sets)

        i=0
        head2=None
        for x in sets:
            if i>0:
                node=ListNode(x)
                cur.next = node;
                cur=cur.next
            else:
                head2=ListNode(x)
                cur=head2
            i+=1

        return head2

va = ListNode(-1)
va.next = ListNode(0)
va.next.next=ListNode(0)
va.next.next.next=ListNode(3)

a = Solution()
print a.deleteDuplicates(va)