# moving all zero element in the last of all non zero element without using any extra space  

def Move_zeros(arr):
    insert_index = 0
    for i in range(0,len(arr)):
        if arr[i] != 0:
            arr[insert_index],arr[i] = arr[i],arr[insert_index] 
            insert_index += 1
    return arr
arr = [1,0,5,0,6,0,4]

print(Move_zeros(arr))
