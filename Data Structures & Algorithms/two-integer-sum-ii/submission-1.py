class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        coll = {}
        for index, value in enumerate(numbers):
            if target - value in coll:
                return [coll[target - value], index + 1]

            coll[value] = index + 1

        return []