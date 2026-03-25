def Two_sum(arr,target):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return [i,j]
    return 
arr = [3,2,1,4]
target = 6  
print(Two_sum(arr,target))  
