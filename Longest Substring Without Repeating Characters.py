#Longest Substring Without Repeating Characters
#问题描述
#Given a string, find the length of the longest substring without repeating characters.
#最长不重复字母长度

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s)<=1:
            return len(s)
        maxlen=1
        lists=[s[0]]
        for x in range(len(s)):
            if x>0:
                if s[x] not in lists:
                    lists.append(s[x])
                    if len(lists)>maxlen:
                        maxlen=len(lists)
                else:
                    lists.append(s[x])
                    lists=lists[lists.index(s[x])+1:]
        return maxlen
        
a=Solution()
print a.lengthOfLongestSubstring('agnwaengonaelig')