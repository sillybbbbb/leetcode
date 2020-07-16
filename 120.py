'''
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

 

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

 

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''

class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 0:
            return 0
        dp = [0]
        for i in range(n):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += dp[j]
                elif j == i:
                    triangle[i][j] += dp[-1]
                else:
                    triangle[i][j] += min(dp[j-1],dp[j])

            dp = triangle[i]
        print(triangle)
        return min(triangle[-1])

s = Solution()
triangle = [[-1],[3,2],[-3,1,-1]]
ans = 1-((5/7)**3+(1/7)*(6/7)**2)
print(ans)
#print(s.minimumTotal(triangle))