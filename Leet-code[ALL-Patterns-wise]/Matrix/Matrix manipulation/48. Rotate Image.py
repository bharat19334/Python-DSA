# brute force approach
# (but this approach is not inplace)
def rotate(matrix):
        
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    n = len(matrix[0])
    for r in range(0,len(matrix)):
        for c in range(0,len(matrix[0])):
            new_matrix[c][(n-1)-r] = matrix[r][c]
           
    return new_matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))

# optimal (inplace)

# 1) first I will find the transpose of given matrix.
# 2) by using draw an dry run diagram we can find pattern.
# 3) pattern is after transpose all reverse row are equal to rotate array by 90 deg.


def rotate(matrix):
        
    n = len(matrix)
    for i in range(0,n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for r in range(0,n):
        matrix[r].reverse()
    return matrix
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))