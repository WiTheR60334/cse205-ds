class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1,cnt={},0
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
            cnt=max(cnt,dict1[i])
        print(dict1)
        dict1 = dict(sorted(dict1.items()))
        print(dict1)
        ans=[]
        for i,freq in dict1.items():
            if k>0:
                ans.append(i)
                k-=1
            else:
                break
        return ans