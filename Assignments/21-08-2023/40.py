class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def rec(start,curr,totalSum):
            if totalSum>target:
                return
            if totalSum==target:
                return ans.append(curr) 
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                rec(i+1,curr+[candidates[i]],totalSum+candidates[i])    
        candidates.sort()        
        rec(0,[],0)
        return ans        