class Solution(object):
    def intersection(self, nums1, nums2):
        # set(nums1)
        # set(nums2)
        return list(set(nums1)&set(nums2))
        # return res
        # return set(nums1).intersection(set(nums2))
        # return nums1&nums2
        