'''
974. 和可被 K 整除的子数组
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

 

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

'''
#超时
class Solution:
    def subarraysDivByK(self, A,K):
        def dp(a,b):
            if b==0:
                return 1 if A[b]%K ==0 else 0
            cnt = 0
            s = A[b]
            if s%K ==0:
                cnt+=1
            for i in range(b-1,-1,-1):
                s += A[i]
                if s%K==0 :
                    cnt +=1

            return dp(a,b-1) + cnt
        return dp(0,len(A)-1)

#前缀法
class Solution2:
    def subarraysDivByK(self, A,K):
        cnt =0
        dic = {0:1}
        presum = 0
        for i in range(len(A)):
            presum += A[i]
            presum %= K
            if presum in dic:
                cnt+=dic[presum]
                dic[presum] +=1
            else:
                dic[presum] = 1
        return cnt

s = Solution2()
A =  [4,5,0,-2,-3,1]
K = 5
print(s.subarraysDivByK(A,K))
