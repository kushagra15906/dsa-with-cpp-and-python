class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        k=max(candies)
        l=[]
        for i in range(0,len(candies),1):
            if (candies[i]+extraCandies)>=k:
                l.append(True)
            else:
                l.append(False)
        return l