class Solution(object):
    def thirdMax(self, nums):
        nums=sorted(set(nums),reverse=True)
        nums=list(nums)
        if len(nums)<=2:
            return max(nums)
        # k=max(nums)
        # nums.remove(k)
        # l=max(nums)
        # nums.remove(l)
        # p=max(nums)
        return nums[2]

        