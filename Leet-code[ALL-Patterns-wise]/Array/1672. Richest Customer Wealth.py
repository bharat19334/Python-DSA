# Brute Force 
class Solution(object):
    def maximumWealth(self, accounts):
        ans = []
        sum = 0
        for n in accounts:
            for i in n:
                sum += i
                ans.append(sum)
            sum = 0
        return max(ans)

# optimal

class Solution(object):
    def maximumWealth(self, accounts):
        sum = 0
        max = float("-inf")
        for n in accounts:
            for i in n:
                sum += i
            if sum > max:
                max=sum
            sum = 0
        return max

        