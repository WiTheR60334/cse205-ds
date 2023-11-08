class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tp=sorted(nums)
        temp=tp[-2:]
        temp=[x-1 for x in temp]
        return temp[0]*temp[-1]