#Valid Palindrome
#问题描述
#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#判断是否回文，符号不检查
#思路:过滤字符串，翻转相等

class Solution:
    # @param s, a string
    # @return a boolean
    def OnlyCharNum(self,s):
        s = s.lower()
        fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for c in s:
            if not c in fomart:
                s = s.replace(c,'')
        return s
    def isPalindrome(self, s):
        s=self.OnlyCharNum(s)
        if s==s[::-1]:
            return True
        else:
            return False

a = Solution()
print  a.isPalindrome('abcdcba')