class Solution(object):
    def maxProduct(self, n):
        l=[]
        while(n!=0):
            r=n%10
            l.append(r)
            n=n/10
        k=max(l)
        l.remove(k)
        p=max(l)
        return k*p