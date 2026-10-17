class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums)
        a=0
        for i in range(n):
            if n%(i+1)==0:
                a+=nums[i]**2
        return a
        