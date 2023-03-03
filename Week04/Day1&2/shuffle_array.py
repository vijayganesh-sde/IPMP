import random
class Solution:
    def __init__(self, nums):
        self.nums=nums
        self.temp=nums
    def reset(self):
        return self.temp
    def shuffle(self) :
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums