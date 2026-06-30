# its brute force by Array pattern but the optimal is possible by hashmap/hashset

class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False