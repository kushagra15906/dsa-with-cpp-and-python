class Solution(object):
    def numberOfSpecialChars(self, word):
        l=list(set(word))
        al=[]
        for i in l:
            al.append(ord(i))
        c=0
        for i in al:
            if i-32 in al:
                c+=1
        return c
        
        