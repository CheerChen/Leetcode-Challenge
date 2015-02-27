#Minimum & Maximum Depth of Binary Tree
#问题描述
#Given a binary tree, find its minimum depth.
#获取最短、最长路径长
#BFS和DFS

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root:
            depth=1
            queue = [(root,depth)]
            while queue:
                node,depth = queue.pop(0)
                if node.left is node.right is None:
                    return depth
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))
        return 0

    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root:
            depth=1
            stack = [(root,depth)]
            depths=[]
            while stack:
                node,depth = stack.pop()
                if node.left is node.right is None:
                    depths.append(depth)
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right, depth+1))
            return max(depths)
        return 0
        
a=Solution()
t=TreeNode(1)
t.left=TreeNode(4)
t.right=TreeNode(8)
t.left.left=TreeNode(11)
t.left.left=TreeNode(11)
# t.right.right=TreeNode(12)
# t=None

# print a.minDepth(t)
print a.maxDepth(t)