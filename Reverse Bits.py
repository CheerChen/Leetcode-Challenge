#Reverse Bits 
#问题描述
#Reverse bits of a given 32 bits unsigned integer.
#反转二进制数
#基本字符串操作

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin=self.dec2bin(n).zfill(32)
        bin=bin[::-1]
        return self.bin2dec(bin)
        
    def dec2bin(self,string_num):
        return str(bin(string_num))[2:]
        
    def bin2dec(self,string_num):
        return int(string_num, 2)
        
a= Solution()
print a.reverseBits(43261596)