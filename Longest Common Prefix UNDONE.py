class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==1:
            return strs[0]
        # strs=sorted(strs)
        # ret=''
        # for x in range(len(strs)):
        #     if x>0:
        #         prefix=self.commonPrefix(strs[x],strs[x-1])
        #         if prefix:
        #             if len(prefix)>len(ret):
        #                 ret=prefix
        #         else:
        #             ret=''
        # return ret
    def commonPrefix(self,strs):
        p=1
        ret=''
        for x in strs:
            if strs[0][0:p] in x:
                ret=strs[0:p]
            else:
                break
        return ret


a=Solution()
print a.commonPrefix(['a'])