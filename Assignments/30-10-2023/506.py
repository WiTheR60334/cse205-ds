class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp=sorted(score)[::-1]
        medals=["Gold Medal","Silver Medal","Bronze Medal"]
        dict={}
        for i in temp:
            if medals:
                dict[i]=medals[0]
                medals.pop(0)
            else:
                dict[i]=str(temp.index(i)+1)
        ans=[]
        for i in score:
            ans.append(dict[i])
        return ans