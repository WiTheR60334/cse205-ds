class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a,b = len(matrix),len(matrix[0])
        ans = []
        for i in range(b):
            arr = []
            for j in range(a):
                arr.append(matrix[j][i])
            ans.append(arr) 
        return ans