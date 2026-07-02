def findMissingAndRepeatedValues(grid):
    
    ans1 = 0
    ans2 = 0
    hash_dict = {}
    keys = []
    for n in grid:
        for m in n:
            hash_dict[m] = hash_dict.get(m,0)+1
    for key,value in hash_dict.items():
        keys.append(key)
        if value >=2:
            ans2 = key
    for i in range(1,len(keys)+2):
        if i not in keys:
            ans1 = i
    return [ans2,ans1]
    
grid = [[9,1,7],[8,9,2],[3,4,6]]
print(findMissingAndRepeatedValues(grid))