'''
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''



class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        k = int((l1+l2)/2)
        odd = (l1+l2)%2
        
        def getKthnum(k):
            index1, index2 = 0, 0
            while True:

                if index1 == l1:
                    return nums2[index2+k-1]
                if index2 == l2:
                    return nums1[index1+k-1]
                if k <= 1:
                    return int(min(nums1[index1], nums2[index2]))
                t1 = int(k//2)
                new1= min(index1+t1-1,l1-1)
                new2 = min(index2+t1-1,l2-1)
                if nums1[new1] <nums2[new2]:
                    k -= new1-index1+1
                    index1 = new1+1 
                    
                else:
                    k -= new2-index2+1
                    index2 = new2+1
                    
                
        if odd: #奇数
            print(getKthnum(k+1))
            
        else:
            print((getKthnum(k)+getKthnum(k+1))/2)

class Solution2:
    def findMedianSortedArrays(self, nums1, nums2): 
        l1 = len(nums1)
        l2 = len(nums2)
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        k = (l1+l2+1)//2
        odd = (l1+l2)%2
        infinty = 2**40
        left = 0
        
        right = l1
        ansi = -1

        while left<=right:
            print(left,right)
            i =(left + right) // 2
            j = (l1 + l2 + 1) // 2 - i
            print(j)
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == l1 else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == l2 else nums2[j])

            if nums_im1 <= nums_j:
                ansi = i
                left = i+1
            else:
                right = i-1
            print(left,right)
        i = ansi
        j = k-i
        left1 = nums1[i-1] if i>0 else -999999
        left2 = nums2[j-1] if j>0 else -999999
        right1 = nums1[i] if i!=l1 else 999999
        right2 = nums2[j] if j!= l2 else 9999999
        if odd: #奇数

            print(max(left1,left2))
            
        else:
            print((max(left1,left2)+min(right1,right2))/2)





s = Solution2()
nums1 = [1,3,4]
nums2 = [5]#
print(s.findMedianSortedArrays(nums1,nums2))