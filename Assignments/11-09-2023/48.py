class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,a = 0,len(matrix) -1
        while l < a:
            matrix[l] , matrix[a] = matrix[a] , matrix[l]
            l +=1
            a -=1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j] , matrix[j][i]= matrix[j][i] , matrix[i][j]
