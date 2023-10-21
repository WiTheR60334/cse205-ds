class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp,ans={},[]
        for i in nums:
            if i not in temp:
                temp[i]=1
            else:
                temp[i]+=1
        while k>0:
            max_key = max(temp, key=temp.get)
            ans.append(max_key)
            del temp[max_key]
            k-=1
        return ans