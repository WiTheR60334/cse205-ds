class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x,y=[],[]
        for i in range(len(s)):
            if x and s[i]=="#":
                x.pop()
            else:
                if s[i]!="#":
                    x.append(s[i])
        for i in range(len(t)):
            if y and t[i]=="#":
                y.pop()
            else:
                if t[i]!="#":
                    y.append(t[i])
        if x==y:
            return True
        return False