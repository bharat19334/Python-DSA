class Solution(object):
    def majorityElement(self, nums):
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if nums[i]==nums[j]:
                    count +=1
            if count > len(nums)//2:
                return nums[i]
            else:
                count = 0

            
