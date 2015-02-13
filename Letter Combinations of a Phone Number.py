#Letter Combinations of a Phone Number
#问题描述
#Given a digit string, return all possible letter combinations that the number could represent.
#给出所有的字母组合

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        letters=[[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        if len(digits)==0:
            return ['']

        #add letters into queues
        lists=[]
        for x in digits:
            if x in map(str,range(10)):
                lists.append(letters[int(x)])
        
        if len(lists):
            lists=self.perm(lists)
        return lists
        
    def perm(self,lists):
        ret=lists[0]
        for x in range(len(lists)):
            if x>0:
                ret=self.comb(ret,lists[x])
        return ret
                
    
    def comb(self,x1,x2):
        temp=[]
        for x in x1:
            for y in x2:
                temp.append(x+y)
        return temp