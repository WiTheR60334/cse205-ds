class Solution:
    def subsets(self, nums):
        n = len(nums)
        subsets = []
        for i in range(1 << n):
            sub = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    sub.append(nums[j])
            subsets.append(sub)
        return subsets
