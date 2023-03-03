class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        sum=0
        while nums and len(nums)>1:
            for i in range(len(nums)):
                sum+=nums[i]
                if i>=1 and sum%k==0:
                    print(sum)
                    return 1
            for i in range(len(nums)-1):
                sum-=nums[i]
                if len(nums)-i>2 and sum%k==0:
                    print(sum)
                    return 1
            sum=0
            nums=nums[1:len(nums)-1]
        return 0