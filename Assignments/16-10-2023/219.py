class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in temp and i - temp[num] <= k:
                return True
            temp[num] = i
        return False