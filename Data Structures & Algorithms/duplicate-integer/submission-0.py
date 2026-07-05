class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for key , _ in c.items():
            if c[key] > 1:
                return True
        return False
        