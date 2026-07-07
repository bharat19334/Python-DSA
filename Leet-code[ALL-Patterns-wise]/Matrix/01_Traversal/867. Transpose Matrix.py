def transpose(matrix):
    
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

matrix = [[1,2,3,4,5,6],[4,5,6,7,8,9],[7,8,9,10,11,12]]
print(transpose(matrix))