class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix: 
            ans += matrix[0]
            matrix.pop(0) 
            if matrix:
                for i in matrix: 
                    if i:
                        ans.append(i.pop())
            if matrix and matrix[-1]: 
                ans += matrix[-1][::-1]
                matrix.pop() 
            if matrix:
                for i in matrix[::-1]:
                    if i:
                        ans.append(i.pop(0))
        return ans