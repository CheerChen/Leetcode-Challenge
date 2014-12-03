#Palindrome Number
#问题描述
#Determine whether an integer is a palindrome. Do this without extra space.
#检查回文整数
#直接转字符串是否相等,感觉这样做是有点low,用时1700+ms


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            if str(x)==str(x)[::-1]:
                return True
            else:
                return False