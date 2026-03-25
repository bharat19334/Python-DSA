def Two_sum(arr,target):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return [i,j]
    return 
arr = [4,-2,5,0,6,3,2,7]
target = 1
print(Two_sum(arr,target))