class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # dictionary to store numbers and their indices
        for i in range(len(nums)):
            diff = target - nums[i]   # what we need to reach target
            if diff in seen:          # check if the complement exists
                return [seen[diff], i]  # return the two indices
            seen[nums[i]] = i          # store the current number and its index
