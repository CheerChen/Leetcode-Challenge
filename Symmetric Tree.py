#Symmetric Tree
#问题描述
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#判断树是否对称
#生成树的序列，用序列判断对称

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root, withemptynode=False):
        if root:
            LOT=[]
            depth=0
            queue = [(root,depth)]
            while queue:
                node,depth = queue.pop(0)
                if len(LOT)!=depth+1:
                    LOT.append([])
                LOT[depth].append(node.val if node else None)
                if node:
                    if node.left:
                        queue.append((node.left, depth+1))
                    elif withemptynode:
                        queue.append((None, depth+1))
                    if node.right:
                        queue.append((node.right, depth+1))
                    elif withemptynode:
                        queue.append((None, depth+1))
            return LOT
        return []
    
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        l=self.levelOrder(root,True)
        if l:
            l=l[:-1]
        print l
        for x in l:
            if x!=x[::-1]:
                return False
        return True
    
    def createTree(self,lists):
        if lists:
            root=TreeNode(lists[0])
            lists.pop(0)
            queue=[root]
            while queue:
                node = queue.pop(0)
                if lists:
                    val=lists.pop(0)
                    if val!='#':
                        node.left=TreeNode(val)
                        queue.append(node.left)
                if lists:
                    val=lists.pop(0)
                    if val!='#':
                        node.right=TreeNode(val)
                        queue.append(node.right)
            return root
        return None

a=Solution()
t=a.createTree([1,2,2,3,3,3,3,4,4,4,4,4,4,'#','#',5,5])
print a.isSymmetric(t)