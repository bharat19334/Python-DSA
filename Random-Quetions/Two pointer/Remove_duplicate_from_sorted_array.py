def duplicate(nums):
        i = 0
        unique = 1
        count = 1
        if len(nums)==1:
            return nums
        while i<=len(nums)-2:
            if nums[i]!=nums[i+1]:
                nums[unique] = nums[i+1]
                unique+=1
                count +=1
            i+=1
        return f"{nums[:unique]},total unique element count : {count}"
       
nums=[1,1,1,2,2,3,3]
print(duplicate(nums))