class Solution(object):
    def majorityElement(self, nums):
        nums=sorted(nums)
        l=list(set(nums))
        a=[]
        for i in range(len(l)):
             if nums.count(l[i])>len(nums)/2:
                a.append(l[i])
        return max(a)

        