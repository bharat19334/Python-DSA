# Marking pattern
def set_matrix_zeros(matrix):
    ans = []
    row = set()
    columns = set()
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i) 
                columns.add(j)  
                  
    for r in row:
        for i in range(len(matrix[0])):
            matrix[r][i] = 0
    for c in columns:
        for i in range(len(matrix)):
            matrix[i][c] = 0
            
    return matrix
                
    
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_matrix_zeros(matrix))