class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        def rec(i,ans):
            if i>=len(words):
                return ans==s
            a=words[i]
            b=a[0]
            temp=ans+b
            return rec(i+1,temp)
        return rec(0,"")   