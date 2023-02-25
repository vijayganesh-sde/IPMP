class Solution:
    def subarraySum(self, nums, k: int) -> int:
      d={0:1}
      sum=0
      count=0
      for i in range(len(nums)):
        sum+=nums[i]
        if sum-k in d:
            count+=d[sum-k]
        if sum not in d:
            d[sum]=1
        else:
            d[sum]+=1
      return count