class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi_num=min(nums)
        max_nums=max(nums)
        for i in nums:
            if i != mi_num and i !=max_nums:

                
                return i
        return -1
            