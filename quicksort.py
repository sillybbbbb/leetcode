import random

def findKthLargest(nums, k: int) -> int:
    size = len(nums)
    target  = size-k
    low = 0
    high = size-1

    while 1:
        index = getindex(nums,low,high)
        if index == target:
            return nums[target]
        elif index<target:
            low = index+1
        else:
            high = index-1
    

def qsmain(nums):
    length = len(nums)

    low = 0
    high = length-1
    quicksort(nums,low,high)

def quicksort(nums,low,high):
    if low< high:
        index = getindex(nums,low,high)
    
        quicksort(nums,low,index)
        quicksort(nums,index+1,high)
    print(nums)

def getindex(nums,left,right):
    random_index = random.randint(left, right)
    nums[random_index], nums[left] = nums[left], nums[random_index]

    pivot = nums[left]
    j = left
    for i in range(left + 1, right + 1):
        if nums[i] < pivot:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[left], nums[j] = nums[j], nums[left]
    return j



#nums = [5,1,7,8,1,3,6,15,34,0,22]
#qsmain(nums)
print(findKthLargest([99,
],1))