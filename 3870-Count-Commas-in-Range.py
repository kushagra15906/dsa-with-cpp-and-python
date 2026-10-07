class Solution(object):
    def countCommas(self, n):
        c=0
        if n<1000:
            return 0
        else:
            return n-999
        