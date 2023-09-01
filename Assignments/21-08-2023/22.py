class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def rec(lcount,rcount,tmp):
            if lcount==0 and rcount==0:
                ans.append(tmp)
            if lcount>0:
                rec(lcount-1,rcount,tmp+"(")
            if rcount>lcount:
                rec(lcount,rcount-1,tmp+")")
        rec(n,n,"")
        return ans