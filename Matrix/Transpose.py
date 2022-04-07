def transpose(matrix):
        l= [[None] * len(matrix) for _ in range(len(matrix[0]))]
        for i,j in product(range(len(matrix)),range(len(matrix[0]))):
            l[j][i]=matrix[i][j]
   
        return l