class Solution:
  def twoSum(self, nums, target: int):
    arr=[]
    l=list(nums)
    for i in list(nums):
      val2=target-i
      l1=list(nums[l.index(i)+1:])
      if val2 in l1:
        if val2==i:
          nums[l.index(i)]=-9
        arr.append(l.index(i))
        arr.append(nums.index(val2))
        return arr