#Reverse Integer
#问题描述
#Reverse digits of an integer.
#反转整型
#思路:转字符反转,再转回int
#点:注意overflow,python会自动把超出的int转成long
#我还以为10整除法比字符转换快,结果两个都是350+ms,呵呵

class Solution:
    # @return an integer
    def reverse(self, x):
        if x>0:
            f=1
        else:
            f=-1
        strs=str(abs(x))
        strs=strs[::-1]
        ints=int(strs)
        if ints>2**31:
            return 0
        return int(strs)*f

    def reverse(self, x):
        if x>0:
            f=1
        else:
            f=-1
        x=abs(x)
        ret=0
        while x/10:
            ret=ret*10+ x%10;
            x=x/10;
        ret =ret*10+x;
        if ret>2**31:
            return 0
        return ret*f