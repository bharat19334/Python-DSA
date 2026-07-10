# without Hashing 
class Solution(object):
    def isAnagram(self, s, t):                     
        sort_t = sorted(t)
        sort_s = sorted(s)
        if len(s)!=len(t):
            return False
        i = 0
        j = 0
        while i<len(s) and j<len(s):
            if sort_s[i]==sort_t[j]:
                i+=1
                j+=1
            else:
                return False
        return True


# By hashing 
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        hash_dict = {}
        for ch in s:
            hash_dict[ch] = hash_dict.get(ch,0)+1

        for ch in t:
            if ch in hash_dict:
                hash_dict[ch] -= 1
            else:
                return False
        for ch in hash_dict.values():
            if ch != 0:
                return False
        return True



        


