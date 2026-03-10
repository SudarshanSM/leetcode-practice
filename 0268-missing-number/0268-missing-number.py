class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        input_sum=n*(n+1)//2
        actual_sum=sum(nums)
        diff=input_sum-actual_sum
        return(diff)

        