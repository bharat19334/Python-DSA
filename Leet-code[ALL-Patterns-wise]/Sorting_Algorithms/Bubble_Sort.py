# Bubble Sort in Non-Decresing Order
def Bubble_sort(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]: 
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
nums = [9,4,15,47,0,3,1,6,4,2]
print(Bubble_sort(nums))

#