class Solution:
    def pivotIndex(self, nums) -> int:
        sum=0
        arr=nums.copy()
        for i in range(len(nums)):
            sum+=nums[i]
            nums[i]=sum
        sum=0
        ind=-1
        for i in range(len(arr)-1,-1,-1):
            sum+=arr[i]
            if nums[i]==sum:
                ind=i
        return ind