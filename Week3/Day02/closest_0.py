import math
class Solution:
  def findClosestNumber(self, nums) -> int:
    min_till=1000000
    for i in range(len(nums)):
        if math.fabs(min_till)==nums[i]:
            min_till=nums[i]
        if math.fabs(nums[i]) < math.fabs(min_till):
            min_till=nums[i]
    return min_till