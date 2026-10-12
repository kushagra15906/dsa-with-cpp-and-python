class Solution(object):
    def findGCD(self, nums):
        k=min(nums)
        p=max(nums)
        for i in range(k,0,-1):
            if k%i==0 and p%i==0:
                return i
        