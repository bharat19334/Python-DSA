class Solution:
    def moveZeroes(self, nums):
        index = 0
        i = 0
        while i<len(nums):
            if nums[i]!=0:
                nums[index],nums[i] = nums[i],nums[index]
                index += 1
            i+=1
        return nums