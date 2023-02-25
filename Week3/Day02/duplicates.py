class Solution:
    def findDuplicates(self, nums) :
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        nums=[]
        for key in d:
            if d[key]==2:
                nums.append(key)
        return nums