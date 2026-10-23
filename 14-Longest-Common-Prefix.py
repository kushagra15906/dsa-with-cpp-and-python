class Solution(object):
    def longestCommonPrefix(self, strs):
        l=sorted(strs)
        a=[]
        k=min(l)
        for i in range(len(k)):
            # if l[i]=="":
                # return ""
            if l[0][i]!=l[-1][i]:
                break
            else:
                a.append(l[0][i])
        return "".join(a)
        