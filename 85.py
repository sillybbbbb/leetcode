

class Solution:
    def maximalRectangle(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        cur_left = 0
        cur_right = n-1
        height,left,right = [0]*m,[0]*m,[m]*m
        maxarea = 0
        for i in range(n):
            cur_left = 0
            cur_right = m
            for j in range(m):
                if matrix[i][j] == '1': 
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(m):
                if matrix[i][j] == '1': 
                    left[j] = max(cur_left,left[j])
                else:
                    cur_left = j+1
                    left[j] = 0
            for j in range(m-1,-1,-1):
                if matrix[i][j] == '1': 
                    right[j] = min(cur_right,right[j])
                else:
                    cur_right = j
                    right[j] = m

            for j in range(m):
                maxarea = max(maxarea, height[j] * (right[j]-left[j] ))
        return maxarea      
s = Solution()
rectangle = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]


print(s.maximalRectangle(rectangle))