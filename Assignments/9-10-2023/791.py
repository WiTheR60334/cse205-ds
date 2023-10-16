class Solution:
    def customSortString(self, order: str, s: str) -> str:
        temp=[i for i in s]
        order=[i for i in order]
        ans=[]
        for i in order:
            while i in temp:
                ans.append(i)
                temp.remove(i)
        return "".join(ans+temp)