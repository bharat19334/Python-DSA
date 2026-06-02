def unique(nums):
    n = []
    for i in nums:
        if i not in n:
            n.append(i)
    return n
nums = [1,2,2,3]
print(unique(nums))