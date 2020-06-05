class Solution:
    def maxSlidingWindow(self,nums,k):
        deque = []
        ret = []
        n=len(nums)
        for i in range(n):
            while(len(deque) and nums[deque[-1]]<nums[i]):
                deque.pop(-1)
            deque.append(i)
            if i>k-2:
                if deque[0]<i+1-k:
                    deque.pop(0)
                ret.append(nums[deque[0]])
        return ret

