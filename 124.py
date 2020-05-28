'''
124. 二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    maxlist =-9999999
    def dfs(self, root: TreeNode):
        if not root:
            return -99999999
        s1 = self.dfs(root.left)
        s2 = self.dfs(root.right)
        x = max(s1+root.val,s2+root.val,root.val)
        self.maxlist = max(self.maxlist,x,s1+s2+root.val)
        return x
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.dfs(root)
        return self.maxlist