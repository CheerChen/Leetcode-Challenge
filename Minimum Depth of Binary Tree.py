#Minimum Depth of Binary Tree
#问题描述
#Given a binary tree, find its minimum depth.
#获取最短路径长
#产生路径集，逐个判断
#bfs快很多

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    # 197ms
    def minDepth(self, root):
        if root:
            paths=self.makePaths(root)
            depths=[]
            for x in paths:
                depths.append(len(x))
            return min(depths)
        return 0
    def makePaths(self,t):
        paths = []
        if not (t.left or t.right):
            return [[t.val]]
        if t.left:
            paths.extend([[t.val] + child for child in self.makePaths(t.left)])
        if t.right:
            paths.extend([[t.val] + child for child in self.makePaths(t.right)])
        return paths
        
    # 82ms
    def minDepth_BFS(self, root):
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

a=Solution()
# t=TreeNode(1)
# t.left=TreeNode(4)
# t.right=TreeNode(8)
# t.left.left=TreeNode(11)
# t.right.right=TreeNode(12)
t=None

print a.minDepth(t)