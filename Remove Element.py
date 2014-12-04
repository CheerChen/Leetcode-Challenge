#Remove Element
#问题描述
#Given an array and a value, remove all instances of that value in place and return the new length.
#去掉指定元素并返回新长度
#思路:注意会检查输入的数组是否去掉了指定元素

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        # return len(A)-A.count(elem)
        while elem in A:
            A.remove(elem)
        return len(A)