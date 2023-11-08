class Solution:
    def largestInteger(self, num: int) -> int:
        temp=[int(x) for x in str(num)]
        ans=0
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if temp[i]%2==0 and temp[j]%2==0:
                    if temp[i]<temp[j]:
                        temp[j],temp[i]=temp[i],temp[j]
                elif temp[i]%2!=0 and temp[j]%2!=0:
                    if temp[i]<temp[j]:
                        temp[j],temp[i]=temp[i],temp[j]
        for i in temp:
            ans=ans*10+i
        return ans