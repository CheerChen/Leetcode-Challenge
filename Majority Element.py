#Majority Element
#问题描述
#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#查找过半的元素
#1思路:排序后取中位数,o(nlogn)
#2思路:过半数出现的次数大与其他元素的次数,一次遍历可以得到,o(n)

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement1(self, num):
        num=sorted(num)
        return num[len(num)/2]

    def majorityElement2(self, num):
    	m=''
    	times=1
        for x in num:
        	if m!=x:
        		times-=1
        		if times==0:
        			m=x
        			times+=1
        	else:
        		times+=1
        return m

a=Solution()
print a.majorityElement2([1,2,1])
print a.majorityElement2([1,2,1,2,2])
