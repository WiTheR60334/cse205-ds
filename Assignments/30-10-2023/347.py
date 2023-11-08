class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        c=sorted(c.items(), key=lambda x: -x[1])
        ans=[]
        for i,freq in c:
            if k>0:
                ans.append(i)
                k-=1
            else:
                break
        return ans