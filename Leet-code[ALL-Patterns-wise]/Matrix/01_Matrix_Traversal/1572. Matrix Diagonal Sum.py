def matrix_diagonal(matrix):
    
    primary_diago = 0
    secondary_diago = 0
    i = 0
    while i<len(matrix[0]):
        primary_diago += matrix[i][i]
        i+=1
        
    j = len(matrix[0])-1    
    m= 0
    while j>=0:
        secondary_diago += matrix[m][j]
        m+=1
        j-=1
    
    remove_ele = len(matrix)//2
    if len(matrix)%2==0:
        return primary_diago+secondary_diago
    else:
        return primary_diago+secondary_diago-matrix[remove_ele][remove_ele]

matrix =   [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]
        ]

print(matrix_diagonal(matrix))

