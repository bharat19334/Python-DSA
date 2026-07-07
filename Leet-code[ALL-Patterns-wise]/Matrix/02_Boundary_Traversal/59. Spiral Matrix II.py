class Solution(object):
    def generateMatrix(self, n):
        top = 0
        left = 0
        right = n-1
        bottom = n-1
        matrix = [[0 for _ in range(n)] for _ in range(n) ]
        m = 1
        
        while left<=right and top<=bottom:

            for i in range(left,right+1):
                matrix[top][i] = m
                m+=1
            top += 1

            for i in range(top,bottom+1):
                matrix[i][right] = m
                m+=1
            right -= 1
            
            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i] = m
                    m+=1
                bottom -= 1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left] = m
                    m+=1
                left += 1
        return matrix

