class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #Create a Hashset 
        hashset = set()
    #loop through the numbers in he given list
        for n in nums:
    #if that particular element is in hash set then return True
            if n in hashset:
                return True
        # if it is not in the hash then add that element in hash for checking in next steps
            hashset.add(n)
        # IF THERE ARE NO DUPLICATED HEN RETURN FALSE
        return False