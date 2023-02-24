class Solution:
    def maximumDifference(self, nums) -> int:
        max_till=-1
        l=0
        r=1
        while r!=len(nums):
            if nums[r]<=nums[l]:
                l=r
                r=l+1
                continue
            if nums[r]-nums[l]>max_till:
                max_till=nums[r]-nums[l]
            r+=1
        return max_till    
        