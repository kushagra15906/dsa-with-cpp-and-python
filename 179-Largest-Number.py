class Solution(object):
    def largestNumber(self, nums):
        l=[]
        n=len(nums)
        for i in nums:
            l.append(str(i))
        if all(x==0 for x in nums):
            return "0"
        for i in range(0,n-1,1):
            for j in range(0,n-i-1,1):
                if (l[j]+l[j+1])<(l[j+1]+l[j]):
                    temp=l[j]
                    l[j]=l[j+1]
                    l[j+1]=temp
        return "".join(l)
        