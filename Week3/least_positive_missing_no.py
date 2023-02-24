class Solution:
    def firstMissingPositive(self, nums) -> int:
        pos_min=1000000
        pos_max=-1
        d={}
        for i in range(len(nums)):
            if nums[i]>0 and pos_min>nums[i]:
                pos_min=nums[i]
            if nums[i]>0 and pos_max<nums[i]:
                pos_max=nums[i]
            if nums[i]>0 and nums[i] not in d:
                d[nums[i]]=1
        if pos_min>1:
            return 1
        for i in range(pos_min,pos_max+1):
            if i not in d:
                return i
        return pos_min-1 or pos_max+1
            
                