class Solution:
    def findMaxLength(self, nums) -> int:
      d={}
      count=0
      max_len=0
      for i in range(len(nums)):
          if nums[i]==0:
              count-=1
          if nums[i]==1:
              count+=1
          if count==0:
              max_len=i+1
          if count in d:
              max_len=max(max_len,i-d[count])
          else:
              d[count]=i
      return max_len