class Solution:
    def threeSum(self, nums):
        nums.sort()
        arr=[]
        if len(nums)==3:
            if sum(nums)==0:
                return [nums]
            return []
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    if [nums[i],nums[l],nums[r]] not in arr:
                        arr.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                if s>0:
                    r-=1
                if s<0:
                    l+=1
        return arr