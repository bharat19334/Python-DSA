# moore's voting algorithum
# optimal
class Solution(object):
    def majorityElement(self, nums):
        freq = 0
        ans = 0
        for i in range(0,len(nums)):
            if freq == 0:
                ans = nums[i]
            if ans == nums[i]:
                freq +=1

            else:
                freq-=1
        return ans
    
    
# brute force Solution
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
        return -1
            
# its best solution as compare to Brute force
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        count = 1
        ans = nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count +=1
            else:
                count = 1
                ans = nums[i]
            if count>len(nums)//2:
                return ans
        return -1