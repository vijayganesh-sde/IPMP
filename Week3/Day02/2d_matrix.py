class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        nums=[]
        for i in range(len(matrix)):
            nums.extend(matrix[i])
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return 1
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return 0