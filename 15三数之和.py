'''
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums) :
        nums.sort()
        
        n = len(nums)
        ans = []
        if n<=2:
            return []
        
        for i in range(n):
            if nums[i]>0 :
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = n-1
            while L<R:
                s = nums[i] + nums[L] + nums[R]
                if  s== 0:
                    if L==i+1 or R == n-1 or  (nums[L] != nums[L-1] and nums[R]!= nums[R+1]):
                        
                        ans.append([nums[i] , nums[L] , nums[R]])
                    L+=1
                    R-=1
                    

                    
                elif s<0:
                    L+=1
                else:
                    R-=1
        return ans

s = Solution()
nums =[0,-4,-1,-4,-2,-3,2]
print(s.threeSum(nums))
