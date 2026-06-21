
def sortedSquares(nums):
    pos = []
    nag = []
    
    for n in nums:
        if n<0:
            nag.append(n**2)
        else:
            pos.append(n**2)
    nag.reverse()
    
    i = 0
    j = 0
    ans = []
    while i<len(pos) and j<len(nag):
        if pos[i]<nag[j]:
            ans.append(pos[i])
            i+=1
        else:
            ans.append(nag[j])
            j+=1
    while i<len(pos):
        ans.append(pos[i])
        i+=1

    while j<len(nag):
        ans.append(nag[j])
        j+=1
    return ans

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
            

        