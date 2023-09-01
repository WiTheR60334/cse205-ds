class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def rec(nums,path):
            if not nums:
                return ans.append(path)
            for i in range(len(nums)):
                rec(nums[:i]+nums[i+1:],path + [nums[i]])
        rec(nums,[])
        return ans        