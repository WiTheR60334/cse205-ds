class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            a,temp = ans[-1],[1]
            for j in range(len(a)-1):
                temp.append(a[j] + a[j+1])
            temp.append(1)
            ans.append(temp)
        return ans