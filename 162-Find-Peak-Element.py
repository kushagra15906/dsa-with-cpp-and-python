class Solution(object):
    def findPeakElement(self, nums):
        k=max(nums)
        return nums.index(k)