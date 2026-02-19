class Solution:
    def is_prime(self,a):
        if a < 2:

            return False
        for i in range (2,int(a**0.5)+1):
            if a % i == 0:
                return False
        return True  

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n=len(nums)
        matr=[]
        for i in range (n):
            matr.append(nums[i][i])
            matr.append(nums[i][n-i-1])
        max_prime=0
        for value in matr:
            if self.is_prime(value):
                max_prime = max(max_prime, value)

        return max_prime

        
        