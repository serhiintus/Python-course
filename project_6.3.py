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