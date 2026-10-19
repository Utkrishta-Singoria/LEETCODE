class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        add = 0
        for i in range(1,n+1):
            if (n % i) == 0:
                add += (nums[i-1])**2
        return add