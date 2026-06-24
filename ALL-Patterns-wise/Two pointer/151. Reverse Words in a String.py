class Solution(object):
    def reverseWords(self, s):
        l = list(s.split())
        
        ans = []
        i = len(l)-1
        while i>=0:
            ans.append(l[i])
            i-=1
        return " ".join(ans)
