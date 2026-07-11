# logic:

# 1) first we need to sort both greedy factor and size of cookies
# 2) Check whether the current cookie size is greater than or equal to the current child's greed factor.
# 3) if its condtion satisfied then we count how many children are happy
# 4) Otherwise, move to the next cookie because the current cookie is too small to satisfy the current child.


class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i = 0
        j = 0
        happy_child = 0
        while i<len(g) and j < len(s):
            if g[i] <= s[j]:
                happy_child +=1
                i+=1
                j+=1
            else:
                j+=1
        return happy_child 
                    
