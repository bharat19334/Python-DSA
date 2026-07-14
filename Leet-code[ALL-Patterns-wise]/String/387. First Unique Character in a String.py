# approach :- Brute Force
# 1) we will count the frequency of each element by nested loop.
# 2) with the each iteration we will check the our frequency count.
# 3) after completing the 1 charactor freq we will check the freq count and if its 1 then return the index of this charactor.
# 3) If its not 1 then we will go through on next charactor.
# 4) after completing all process if unique element doesn't exist then we will return -1.
class Solution(object):
    def firstUniqChar(self, s):
    
        for i in range(0,len(s)):
            count = 0
            for j in range(0,len(s)):
                if s[i]==s[j]:
                    count +=1
            if count == 1:
                return i
        return -1

#Approach: Optimal 
# 1) we will store all frequency in dictionary.
# 2) we will check each charactor freqency in dictionary acording to our string iteration .
# 3) if freq. is 1 then return index value otherwise -1
class Solution(object):
    def firstUniqChar(self, s):
        hash_dict = {}
        for i in range(0,len(s)):
            hash_dict[s[i]] = hash_dict.get(s[i],0)+1
        for i in range(0,len(s)):
            if hash_dict[s[i]] == 1:
                return i
        return  -1