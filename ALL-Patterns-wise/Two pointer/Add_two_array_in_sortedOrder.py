# we have 2 sorted array and return a array which cover both array element in sorted order.
# example:- arr1=[1,5,7], arr2=[2,3,9]
# Output = [1,2,3,5,7,9]

def Add_array(arr1,arr2):
    i = 0
    j = 0
    ans = []
    if a
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
    while i<len(arr1):
        ans.append(arr1[i])
        i+=1
        
    while j<len(arr2):
        ans.append(arr2[j])
        j+=1
    return ans
            
arr1=[1,5,7]
arr2=[2,3,9]
print(Add_array(arr1,arr2))