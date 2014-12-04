#Remove Nth Node From End of List
#问题描述
#Given a linked list, remove the nth node from the end of list and return its head.
#链表中删除倒数n的元素
#思路1:用list装载，pop，再转回链表
#思路2:双指针相隔n同时走，后一个到达链表尾删除前一个指向的元素（一次遍历）


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        pointer=self
        lists=[]
        while pointer is not None:
            lists.append(pointer.val)
            pointer = pointer.next
        print lists

class Solution:
    def removeNthFromEnd(self, head, n):
        pointer=head
        lists=[]
        while pointer is not None:
            lists.append(pointer.val)
            pointer = pointer.next

        lists.pop(len(lists)-n)
        i=0
        head2=None
        for x in lists:
            if i>0:
                node=ListNode(x)
                cur.next = node;
                cur=cur.next
            else:
                head2=ListNode(x)
                cur=head2
            i+=1

        return head2

    def removeNthFromEnd2(self, head, n):
        slow=fast=head
        for i in range(n):
            fast=fast.next
        #if remove the first element
        if fast==None:
            return head.next

        #moving slow and fast pointer in same step
        while fast.next!=None:
            fast=fast.next
            slow=slow.next

        #remove element which slow point to
        slow.next=slow.next.next

        return head

va = ListNode(-1)
va.next = ListNode(0)
va.next.next=ListNode(0)
va.next.next.next=ListNode(3)

a = Solution()
print a.removeNthFromEnd(va,4)