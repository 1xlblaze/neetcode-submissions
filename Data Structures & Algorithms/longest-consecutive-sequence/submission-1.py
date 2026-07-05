class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        output = int()
        for num in nums:
            print(num)
            if num-1 not in nums:
                count = 1 
                tracking = num+1
                while tracking in nums:
                    count+=1
                    tracking +=1
                if count > output:
                    output=count
        return output

            


        