class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l1=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                l1.append(nums[i:j])
        sum=0
        for i in l1:
            square_len_set = (len(set(i)))**2
            sum += square_len_set
        return sum