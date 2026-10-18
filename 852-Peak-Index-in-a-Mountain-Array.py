class Solution(object):
    def peakIndexInMountainArray(self, arr):
        k=max(arr)
        return arr.index(k)
        