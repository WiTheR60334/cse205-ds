class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,list=0,[]
        for i in nums:
            if i==1:
                count+=1
            else:
                count=0
            list.append(count)
        list.sort()    
        return list[-1]       