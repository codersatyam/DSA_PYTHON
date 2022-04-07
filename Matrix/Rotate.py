def rotate(matrix):
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        return matrix    