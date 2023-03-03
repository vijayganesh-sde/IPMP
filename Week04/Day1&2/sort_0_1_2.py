class Solution:
    def sortColors(self, nums) -> None:
        arr=[0,0,0]
        while len(nums)>0:
            val=nums.pop()
            arr[val]+=1
        for i in range(len(arr)):
            nums.extend(arr[i]*[i])