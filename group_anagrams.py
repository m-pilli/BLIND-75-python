from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            lst = [0]*26 #[0,0,----till 26 0's]
            for i in word:
                lst[ord(i)-ord('a')] += 1 #for each word change the 0 to 1 for each upcoming alphabet 
            lst = tuple(lst) # turning list into tuple
            dic[lst].append(word) #add the words in dictionary based on the key , keys in the dic will be the list->tuple of 26 zero's/one's 
                                 # and the values will be the list of the actual words
        return list(dic.values()) #return the values in list

        