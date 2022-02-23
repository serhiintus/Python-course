#This function gets rectangular matrix of integers given as a list of lists
#and returns tuple with the coordinates of the "saddle point" of the given matrix
#or False if such a point does not exist.
def saddle_point(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            flag = True
            ii = 0
            jj = 0
            for ii in range(len(matrix)):
                if matrix[ii][j] >= matrix[i][j] and i != ii:
                    flag = False
            for jj in range(len(matrix[i])):
                if matrix[i][jj] <= matrix[i][j] and j != jj:
                    flag = False
            if flag:
                return (i, j)
    return False
#examples:
print(saddle_point([[0,0,0],[2,1,2],[1,0,1]])) #(1, 1)
print(saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])) #(1, 2)