# brute force solution
nums = [3,0,1,4,2,6]
n = len(nums)
for i in range(0,n+1):
    if i not in nums:
        print(i)
        
# optimal solution
def missing_number(nums):
    freq =  {}
    for i in range(0,len(nums)+1):
        freq[i] = 0
    for num in nums:
        freq[num] = 1
    for k,v in freq.items():
        if v == 0:
            return k
nums = [0,1,2,3,5]
print(missing_number(nums))