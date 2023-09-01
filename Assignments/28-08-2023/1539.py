class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing,i=[],0
        while len(missing)<k+1: 
            if i>arr[-1]:
                missing.append(i)
            else:
                if i not in arr:
                    missing.append(i)  
            i+=1                   
        return missing[k]