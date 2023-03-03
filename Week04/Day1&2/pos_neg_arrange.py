class Solution:
    def rearrangeArray(self, nums) :
        pos=[]
        neg=[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        nums=[]
        for i in range(len(neg)):
            nums.append(pos[i])
            nums.append(neg[i])
        return nums