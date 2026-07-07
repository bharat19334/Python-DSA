
def searchMatrix(smatrix, target):
        
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 18
        
print(searchMatrix(matrix, target))