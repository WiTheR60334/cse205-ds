class Solution:
    def subsets(self, nums): 
        a=[]
        b=[]
        length = len(nums)
        def rec(nums, i, a):
            if i<0 :
                b.append(a)
                return 0
            rec(nums, i-1, a + [nums[i]])    
            rec(nums, i-1, a)
        rec(nums,length-1,a)
        return b  
