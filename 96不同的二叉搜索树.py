'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
'''
(1,2)
21,1n2
(1,2,3)
[[1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]]
(2,3)
2n3,32




'''
import copy
class Tree:    
    def __init__(self,var,a=[],b = []):
        self.var = var
        self.left = a
        self.right = b
        
'''    

class Solution:


  
    def generateTrees(self, n: int):
        dp = [[[]]*(n+1) for i in range(n+1)]
        for i in range(n+1):
             #t = Tree(i)
             dp[i][i] = []
        for i in range(2,n+1):
            for j in range(1,i+1):
                for k in range(j,i+1):
                    tmp = Tree(k)
                    if k > j:
                        s = copy.deepcopy(dp[j][k-1])
                        if len(s):
                             tmp.left.append(s)
                    if k<i:
                        s = copy.deepcopy(dp[j][k-1])
                        if len(s):
                            tmp.right.append(s)
                dp[j][i]=[tmp]
       
        return dp
'''
class TreeNode:    
    def __init__(self,var):
        self.val = var
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        # 对dp进行初始化
        dp = []
        for i in range(0, n+1):   # 初始化dp
            dp.append([])
            for j in range(0, n+1):
                if i == j:
                    dp[i].append([TreeNode(i)])
                elif i < j:
                    dp[i].append([])
                else:
                    dp[i].append([None])
        dp[0][0] = [None]
        for i in range(n-1, 0, -1):  # 自下向上进行循环
            for j in range(i+1, n+1):
                for r in range(i, j+1):   # i-j每一个节点为顶点的情况
                    left = r+1 if r < j else r    # 右边的值需要边界判断，不然会溢出数组
                    for x in dp[i][r-1]:          # 左右子树排列组合   
                        for y in dp[left][j]:
                            node = TreeNode(r)     
                            node.left = x
                            node.right = y
                            if r == j:
                                node.right = None
                            dp[i][j].append(node)      # dp[i][j]添加此次循环的值
        return dp[1][n]
       
s = Solution()
s.generateTrees(3)