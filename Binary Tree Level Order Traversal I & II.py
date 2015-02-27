#Binary Tree Level Order Traversal I & II
#问题描述
#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#生成正反遍历列表

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root:
            LOT=[]
            depth=0
            queue = [(root,depth)]
            while queue:
                node,depth = queue.pop(0)
                if len(LOT)!=depth+1:
                    LOT.append([])
                LOT[depth].append(node.val)

                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))
            return LOT[::-1]
        return []

     def levelOrderBottom(self, root):
        return self.levelOrder(root)[::-1]
        
a=Solution()
t=TreeNode(1)
t.left=TreeNode(4)
t.right=TreeNode(8)
t.left.left=TreeNode(11)
t.left.left=TreeNode(11)
# t.right.right=TreeNode(12)
# t=None

print a.levelOrder(t)