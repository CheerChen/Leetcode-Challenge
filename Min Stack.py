#Min Stack
#问题描述
#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#设计一个栈
#第一版超时,主要原因应该是min()的速度慢
#所以设计了第二版,维护一个最小值,只在插入和弹出时更新
#这个题也不是很严谨..没规定非法值

class MinStack:
    # @param x, an integer
    # @return an integer
    lists=[]
    def push(self, x):
        self.lists.append(x)

    # @return nothing
    def pop(self):
        return self.lists.pop()

    # @return an integer
    def top(self):
        if len(self.lists)>0:
            return self.lists[-1]
        else:
            return None

    # @return an integer
    def getMin(self):
        return min(self.lists)

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self._min = None
        self._lists = []

    def push(self, x):
        if len(self._lists)==0:
            self._min=x
        else:
            if x<self._min:
                self._min=x
        self._lists.append(x)

    # @return nothing
    def pop(self):
        x=self._lists.pop()
        if x==self._min:
            if len(self._lists)>0:
                self._min=min(self._lists)
            else:
                self._min=None

        return x

    # @return an integer
    def top(self):
        if len(self._lists)>0:
            return self._lists[-1]
        else:
            return None

    # @return an integer
    def getMin(self):
        return self._min