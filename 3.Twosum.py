class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousNum = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in previousNum:
                return [previousNum[diff], i]
            previousNum[j] = i
        