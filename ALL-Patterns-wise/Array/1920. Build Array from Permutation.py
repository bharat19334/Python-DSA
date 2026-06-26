# its better solution by array pattern but optimal is not possible by 

class Solution(object):
    def buildArray(self, nums):
        ans = []
        i = 0
        while i<=len(nums)-1:
            ans[i]=nums[nums[i]]
            i+=1
        return ans
    


        