# Selection sort in non-decresing order
def selection_sort(nums):
    for i in range(0,len(nums)):
       
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[min_index]>nums[j]:
                min_index=j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums
nums=[4,5,3,2,8,7,9]
print(selection_sort(nums))


# Selection sort in decresing order
def selection_sort(nums):
    for i in range(0,len(nums)):
        max_index = i
        for j in range(i+1,len(nums)):
            if nums[max_index]<nums[j]:
                max_index = j
        nums[i],nums[max_index] = nums[max_index],nums[i]
    return nums
nums=[4,5,3,2,8,7,9]
print(selection_sort(nums))