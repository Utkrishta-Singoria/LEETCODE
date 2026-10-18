class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        max=0
        sq= list(map(lambda x:x**2,nums))
        # for i in nums:
        #     sq.append(i**2)
        sq.sort(reverse = True)
        if len(nums)%2 == 0:
            mid = (len(nums)//2)
        else:
            mid = (len(nums)//2)+1
        for i in range(0,mid):
            max += sq[i]
        for i in range(mid,len(sq)):
            max -= sq[i]
        return max
