class Solution(object):
    def maxProduct(self, nums):
        k=max(nums)
        nums.remove(k)
        p=max(nums)
        return (k-1)*(p-1)
        