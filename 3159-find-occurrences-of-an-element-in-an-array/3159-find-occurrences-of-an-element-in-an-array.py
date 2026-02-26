class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        position=[]
        for i in range (len(nums)):
            if nums[i]==x:
                position.append(i)
        
        result=[]
        for k in queries:
            if k<= (len(position)):
                result.append(position[k-1])
            else:
                result.append(-1)

        return result