class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        temp,cnt={},0
        for i in nums:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        cnt1,ans=0,[]
        for i,freq in temp.items():
            if freq>1:
                ans.append(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                ans.append(i)
        return ans