class Solution(object):
    def checkDivisibility(self, n):
        s=0
        q=1
        temp=n
        while(temp>0):
            k=temp%10
            s+=k
            q*=k
            temp=temp/10
        p=s+q

        if n%p==0:
            return True
        else:
            return False
        