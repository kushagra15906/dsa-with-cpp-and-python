class Solution(object):
    def plusOne(self, digits):
        n=len(digits)
        res=0
        for i in digits:
            k=i*10
            res=(res*10)+k
        final=(res/10)+1
        r=str(final)
        l=[]
        for i in r:
            l.append(int(i))
        return l
        