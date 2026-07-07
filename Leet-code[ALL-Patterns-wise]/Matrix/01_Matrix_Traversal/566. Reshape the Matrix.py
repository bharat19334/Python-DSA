def matrix_reshape(mat):
    
    new_mat = [[0 for _ in range(c)] for _ in range(r)]
    new_col = 0
    new_row = 0
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            new_mat[new_row][new_col] = mat[i][j]
            new_col +=1
            if c==new_col:
                new_col = 0 
                new_row+=1

    return new_mat

mat = [[1,2],[3,4]] 
r = 2
c = 2
print(matrix_reshape(mat))