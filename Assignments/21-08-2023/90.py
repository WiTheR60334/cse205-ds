class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(start, path, ans):
            ans.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                rec(i+1, path + [nums[i]], ans)
        nums.sort()
        rec(0, [], ans)
        return ans