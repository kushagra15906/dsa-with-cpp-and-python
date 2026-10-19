class Solution(object):
    def containsDuplicate(self, nums):
        k=list(set(nums))
        if len(k)!=len(nums):
            return True
        return False
