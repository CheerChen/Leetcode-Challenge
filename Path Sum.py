#Path Sum
#问题描述
#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.#将链表中的数字相加
#判断树的路径和是否为定值
#产生路径集，逐个判断
#将结果带入dfs递归递减，可以节省部分时间

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root:
            paths=self.makePaths(root)
            for x in paths:
                t_sum=0
                for i in x:
                    t_sum+=i
                if sum==t_sum:
                    return True
        return False

    def makePaths(self,t):
        paths = []
        if not (t.left or t.right):
            return [[t.val]]
        if t.left:
            paths.extend([[t.val] + child for child in self.makePaths(t.left)])
        if t.right:
            paths.extend([[t.val] + child for child in self.makePaths(t.right)])
        return paths
        
    # better in complex tree
    def hasPathSum2(self, root, sum):
        if root is None:
            return False
        stack = [(root, sum)]
        while stack:
            node, _sum = stack.pop()
            if node.left is node.right is None and node.val == _sum:
                return True
            if node.left:
                stack.append((node.left, _sum - node.val))
            if node.right:
                stack.append((node.right, _sum - node.val))
        return False

a=Solution()
t=TreeNode(1)
# t.left=TreeNode(4)
# t.right=TreeNode(8)
# t.left.left=TreeNode(11)

print a.hasPathSum(t,5)