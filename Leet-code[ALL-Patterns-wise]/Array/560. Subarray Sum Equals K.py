# Brute Force

class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        for i in range(0,len(nums)):
            Total = 0
            for j in range(i,len(nums)):
                Total += nums[j]
                if Total == k:
                    count +=1
        return count
    
    
# optimal approach