class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber1(self, num):
        strs=[]
        for x in num:
            strs.append(str(x))
        if len(num)>1:
            strs=sorted(strs,reverse=True)
            loop=True
            # i=0
            while loop:
                # i+=1
                # if i==10:
                #     loop=False
                for x in range(len(strs)):
                    if x>0:
                        c1=len(strs[x])*2>=len(strs[x-1])
                        c2=strs[x]!=strs[x-1]
                        c3=strs[x] in strs[x-1]
                        if c1 and c2 and c3:
                            c4=strs[x-1].index(strs[x])==0
                            c5=int(strs[x-1].replace(strs[x],'',1))<int(strs[x])
                            if c4 and c5:
                                strs[x],strs[x-1]=strs[x-1],strs[x]
                            elif x==len(strs)-1:
                                loop=False
                        elif x==len(strs)-1:
                            loop=False
        return ''.join(strs)
    
    def largestNumber1(self, num):
        strs=[]
        for x in num:
            strs.append(str(x))
        if len(num)>1:
            strs=sorted(strs,reverse=True)
            for x in range(len(strs)):
                    if x>0:
                        prefix=self.commonPrefix(strs[x],strs[x-1])
                        if prefix:
                            pass
    def commonPrefix(self,s1,s2):
        p=1
        ret=False
        if s1==s2:
            return s1
        while s1[0:p]==s2[0:p]:
            ret=s1[0:p]
            p+=1
        return ret

a=Solution()
print a.commonPrefix('112','11222')