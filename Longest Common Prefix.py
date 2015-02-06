#Longest Common Prefix
#问题描述
#Write a function to find the longest common prefix string amongst an array of strings.
#获取一个字符串列表的最长公共前缀
#思路:取第一个元素的第一个字符，与其他元素的同位置字符对比，只要找到不一致的则停止

class Solution:
    # @return a string
    #50ms
    def longestCommonPrefix2(self, strs):
        if len(strs)==0:
            return ''
        
        for i in range(len(strs[0])):
            ch=strs[0][i]
            for j in range(1,len(strs)):
                if i==len(strs[j]) or ch!=strs[j][i]:
                    return strs[0][:i]
        return strs[0]
    
    #70ms        
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        else:
            p=1
            while p<=len(strs[0]):
                if self.commonPrefix(strs,strs[0][0:p]):
                    p+=1
                else:
                    break
            return strs[0][0:p-1]

    def commonPrefix(self,strs,prefix):
        for x in strs:
            if prefix in x and x.index(prefix)==0:
                pass
            else:
                return False
        return True


a=Solution()
print a.longestCommonPrefix2(["abcd","ab",'abc'])
print a.longestCommonPrefix2([""])