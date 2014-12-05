class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None

    sum=0
    def sum(self,p):
        if p.parent is None:
            return sum
        else:
            sum+=p.data
            p=p.parnet

    def insert(self,p):
        if p.parent is None:


    ret=[]
    def findLeafs(self):
        if self.left:
            self.left.dfs()
        if self.left is None and self.right is None:
            self.ret.append(self)
        if self.right:
            self.right.dfs()

head=Node(0)

head.findLeafs()
print head.ret