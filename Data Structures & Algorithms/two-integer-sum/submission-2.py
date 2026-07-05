class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        set1 = {}
        for key, value in enumerate(nums):
            if target - value in set1:
                return [set1[target - value],key]
            set1[value] = key
        return []
                
        