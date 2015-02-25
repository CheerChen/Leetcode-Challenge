#Add Two Numbers
#问题描述
#You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#将链表中的数字相加
#思路:注意进位
#转成数字相加要快很多，因为省去了链表的一些重复操作

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @return a ListNode
    # 283ms
    def addTwoNumbers(self, l1, l2):
        p1=l1
        p2=l2
        head=ListNode(0)
        p=head
        carry=False
        while p1!=None or p2!=None or carry:
            if p1==None and p2==None and carry:
                p.next=ListNode(1)
            # 处理长度不一致
            if p1==None:
                p1=ListNode(0)
            if p2==None:
                p2=ListNode(0)
                
            # 相加
            retval=p1.val+p2.val
            if carry:
                retval+=1
            if retval>=10:
                retval-=10
                carry=True
            else:
                carry=False
            p.next=ListNode(retval)
            p=p.next
            
            # 移动到下一元素
            if p1!=None:
                p1=p1.next
            if p2!=None:
                p2=p2.next
                
        return head.next

    # @return a ListNode
    # 177ms
    def addTwoNumbers2(self, l1, l2):
        # 转成整数
        i1=self.toNumber(l1)
        i2=self.toNumber(l2)
        
        # 相加
        i=i1+i2
        
        # 写入链表
        head=ListNode(i%10)
        i=i/10
        p=head
        while i:
            p.next=ListNode(i%10)
            p=p.next
            i=i/10
        return head
        
    def toNumber(self,ln):
        p=ln
        s=0
        carry=0
        while p!=None:
            s=p.val*pow(10,carry)+s
            p=p.next
            carry+=1
        return s
        
a=Solution()
l1=ListNode(0)
l1.next=ListNode(4)

l2=ListNode(0)
l2.next=ListNode(5)
print a.addTwoNumbers2(l1,l2).next.val