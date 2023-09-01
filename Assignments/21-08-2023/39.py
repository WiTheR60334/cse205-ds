class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def rec(list,curr,totalSum):
            if totalSum>target:
                return
            if totalSum==target:
                return ans.append(curr)
            for i in range(len(list)):
                rec(list[i:],curr+[list[i]],totalSum+list[i])
        rec(candidates,[],0)
        return ans