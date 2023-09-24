class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        temp,max=[],0
        for i in accounts:
            for j in range(len(i)):
                max+=i[j]
            temp.append(max)   
            max=0
        temp.sort()
        return temp[-1]    