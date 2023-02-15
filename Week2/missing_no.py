class Solution:
  def missingNumber(self, nums):
    n=len(nums)
    sum_exp=(n+1)*(n+2)//2
    sum_nums=sum(nums)
    return sum_exp-sum_nums
arr=[1,3,4]
s=Solution()
print(s.missingNumber(arr))
