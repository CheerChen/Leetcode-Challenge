#Roman to Integer
#问题描述
#Given a roman numeral, convert it to an integer.
#转换罗马数为整数,范围1~3999
#难点:list必须满足右加左减,所以把减数作为一个元素加到list
#顺便做了反向转换

class Solution:
    # @return an integer
    def romanToInt(self, s):
        romanNums=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        intNums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ret=0
        for i in range(len(romanNums)):
            numchrs = len(romanNums[i])
            while s[0:numchrs]==romanNums[i]:
                ret+=intNums[i]
                s=s[numchrs:len(s)]
                if len(s)<=0:
                    break
        return ret

    # @return an string
    def intToRoman(self, s):
        romanNums=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        intNums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ret=''
        for i in range(len(romanNums)):
            while s>=intNums[i]:
                ret=ret+romanNums[i]
                s=s-intNums[i]
                if s<0:
                    break
        return ret
