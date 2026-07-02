# Brute force solution

class Solution(object):
    def productExceptSelf(self, nums):
        ans = []
        for i in range(0,len(nums)):
            prefix = 1
            suffix = 1
            for n1 in range(i-1, -1, -1):
                prefix *= nums[n1]
            for n2 in range(i+1,len(nums)):
                suffix *= nums[n2]
            ans.append(prefix*suffix)
        return ans
    
# optimal solution need o(n) T.C.