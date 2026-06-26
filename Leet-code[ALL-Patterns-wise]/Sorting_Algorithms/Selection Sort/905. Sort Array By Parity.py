# using Selection SORT 

class Solution(object):
    def sortArrayByParity(self, nums):
        if len(nums)==0:
            return [0]
        for i in range(0,len(nums)):
            even_num = i
            for j in range(i+1,len(nums)):
                if nums[j]%2==0:
                    even_num = j
            nums[i],nums[even_num]=nums[even_num],nums[i]
        return nums
    