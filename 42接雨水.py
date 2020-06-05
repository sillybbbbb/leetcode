'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

class Solution:
    def trapp(self, height) -> int:
        stack=[0]
        total = 0
        nowh = 0
        for i in range(1,len(height)):
            while len(stack) and height[stack[-1]] <height[i]:
                
                nowh = stack.pop(-1)
                if stack==[]:
                    break
                total+=(i-stack[-1]-1)*(min(height[i],height[stack[-1]])-height[nowh])
            stack.append(i)
        return total
    #动态规划----------------------------------------------------------
    def trap(self,height):
        n = len(height)
        if n==0:
            return 0
        water = 0
        left = [None]*(n)
        right = [None]*(n)
        left[0] = height[0]
        right[n-1] = height[n-1]
        for i in range(1,n):
            left[i] = max(left[i-1],height[i])
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],height[i])
        for i in range(n):
            water+=max(min(left[i],right[i])-height[i],0)
        return water
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
