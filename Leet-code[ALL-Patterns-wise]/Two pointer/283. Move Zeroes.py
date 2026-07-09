# 1st approach
def moveZeroes(self, nums):
    index = 0
    i = 0
    while i<len(nums):
        if nums[i]!=0:
            nums[index],nums[i] = nums[i],nums[index]
            index += 1
        i+=1
    return nums


# 2nd approach

def moveZeroes(self, nums):
    index = 0
    i = 0
    while i<len(nums):
        if nums[i]!=0:
            nums[index]=nums[i]
            index+=1
        i+=1

    while index<len(nums):
        nums[index]=0
        index+=1
        
    return nums
    
