class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        #loops through both s and t , counts frequency in s & t
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            #comparing frequency
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True