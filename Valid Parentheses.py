#Valid Parentheses
#问题描述
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#判断括号匹配
#思路:学过编译原理的都知道，用栈
#思路:还有一种奇葩的解法，递归替换[]{}()

class Solution:
    # @return a boolean
    def isValid(self, s):
        manList=['[','(','{']
        womanList=[']',')','}']
        stacks=[]
        for c in s:
            if c in manList:
                stacks.append(c)
            if c in womanList:
                if len(stacks) and manList[womanList.index(c)] == stacks[-1]:
                    stacks.pop()
                else:
                    return False
        if len(stacks):
            return False
        return True

    def isValid2(self, s):
        if s == "":
            return True
        if len(s) % 2 == 1:
            return False

        else:
            while(  "()" in s or "[]" in s or "{}" in s):
                s = s.replace("()", "")
                s = s.replace("[]", "")
                s = s.replace("{}", "")
                return self.isValid(s)
            return False

a = Solution()
print  a.isValid(']')