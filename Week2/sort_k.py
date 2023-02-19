import heapq
class Solution:
  def sortArray(self, nums):
    heapq.heapify(nums)
    print(nums)
    return heapq.nsmallest(len(nums),nums)