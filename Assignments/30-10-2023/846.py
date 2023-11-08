class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c= Counter(hand)
        while c:
            n=groupSize
            minimum=min(c.keys())
            while n:
                if minimum not in c:
                    return False
                c[minimum]-=1
                if not c[minimum]:
                    del c[minimum]
                minimum+=1
                n-=1
        return True