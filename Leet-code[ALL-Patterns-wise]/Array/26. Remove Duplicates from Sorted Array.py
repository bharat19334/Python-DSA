def remove(nums):
    i = 0
    j = 1
    count = 1
    while i<(len(nums)-1) and j<len(nums):
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            count += 1
            i+=1
        j+=1
    return nums[:count]
nums = [0,0,1,1,1,2,2,3,3,4]
print(remove(nums))