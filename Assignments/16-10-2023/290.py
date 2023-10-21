class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp={}
        temp1=[i for i in pattern]
        temp2=s.split()
        if len(temp1)!=len(temp2):
            return False
        for i in range(len(temp1)):
            if temp1[i] not in temp:
                if temp2[i] in temp.values():
                    return False
                temp[temp1[i]]=temp2[i]
        a=[]
        for i in temp1:
            a.append(temp[i])
        for i in range(len(a)):
            if a[i]!=temp2[i]:
                return False
        return True