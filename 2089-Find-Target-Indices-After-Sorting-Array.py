class Solution(object):
    def targetIndices(self, nums, target):
        k=sorted(nums)
        l=[]
        for i in range(len(nums)):
            if k[i]==target:
                l.append(i)
        return l

        