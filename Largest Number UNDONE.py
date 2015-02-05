class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        strs=[]
        for x in num:
            strs.append(str(x))
        if len(num)>1:
            strs=sorted(strs,reverse=True)
            ret=''
            lstack=[]
            for x in range(len(strs)):
                    if x>0:
                        # prefix=self.commonPrefix(strs[x],strs[x-1])
                        # print prefix
                        if strs[x][0:1]==strs[x-1][0:1]:
                            if x==1:
                                lstack.append(strs[x-1])
                            lstack.append(strs[x])
                        else:
                            if len(lstack)>0:
                                # print lstack
                                ret+=self.findLargest(lstack)
                                lstack=[]
            if len(lstack)>0:
                ret+=self.findLargest(lstack)
                lstack=[]
            strs=[ret]

        return ''.join(strs)
        
    def commonPrefix(self,s1,s2):
        p=1
        ret=False
        if s1==s2:
            return s1
        while s1[0:p]==s2[0:p]:
            ret=s1[0:p]
            p+=1
        return ret
        
    def perm(self,l):
        if(len(l)<=1):
            return [l]
        r=[]
        for i in range(len(l)):
            s=l[:i]+l[i+1:]
            p=self.perm(s)
            for x in p:
                r.append(l[i:i+1]+x)
        return r

    def findLargest(self,lstack):
        ret=self.perm(lstack)
        temp=[]
        for x in ret:
            temp.append(''.join(map(str,x)))
        return str(max(map(int,temp)))

        
a=Solution()
print a.largestNumber([12,123,1212])
# print a.arrayReplace(12,0,[121,12,12])