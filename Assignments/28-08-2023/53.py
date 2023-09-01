class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, ans = 0 , -10000
        for i in range(len(nums)):
            s += nums[i]
            if s > ans: 
                ans = s
            if s < 0:
                s = 0
        return ans