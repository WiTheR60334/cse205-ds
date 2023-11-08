class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp=sorted(stones)
        while len(temp)>1:
            a=temp.pop()
            b=temp.pop()
            if a!=b:
                a-=b
                temp.append(a)
                temp=sorted(temp)
        return temp[0] if temp else 0