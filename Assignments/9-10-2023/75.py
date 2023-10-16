class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n):
            temp=i
            for j in range(i+1,n):
                if nums[temp]>nums[j]:
                    temp=j
            nums[i],nums[temp]=nums[temp],nums[i]
        # nums.sort()