class Solution:
    def sortArrayByParity(self, nums):
        d={'o':[],'e':[]}
        for i in range(len(nums)):
            if nums[i]%2:
                d['o'].append(nums[i])
            else:
                d['e'].append(nums[i])
        return d['e']+d['o']
