from functools import reduce
import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = reduce(lambda x,y: x*y, nums, 1)
        output = []
        for i in nums:
            if i==0:
                referece = copy.copy(nums)
                referece.remove(0)
                output.append(reduce(lambda x,y: x*y, referece, 1))
            else:
                output.append(product//i)

        return output


        