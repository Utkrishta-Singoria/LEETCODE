# class Solution:
#     def sortableIntegers(self, nums: list[int]) -> int:
#         n = len(nums)
#         k = []
#         ans = 0
#         for i in range(1,n+1):
#             if n % i == 0:
#                 k.append(i)
#         issorted = nums.copy()
#         issorted.sort()
#         if issorted == nums:
#             return sum(k) 
#         subarray=[]
#         for i in range(0,n+1):
#             for j in range(i+1,n+1):
#                 if len(nums[i:j]) in k:
#                     subarray.append(nums[i:j])
#         for i in subarray:
#             p = i.copy()
#             p.sort()
#             if len(i)>1:
#                 for j in range(len(i)):
#                     if (i == p) and (len(i) in k):
#                         ans+=len(i)
#                         k.remove(len(i))
#                         break
#                     i = i[-1:] + i[:-1]
#         return ans
class Solution:
    def check(self, nums, length):
        n = len(nums)
        minn = 0
        
        for i in range(0, n, length):
            if nums[i] < minn:
                return False
            
            maxx = nums[i]
            point = False
            
            for j in range(i + 1, i + length):
                if nums[j] < minn:
                    return False
                
                if nums[j - 1] > nums[j]:
                    if point:
                        return False
                    point = True
                
                maxx = max(maxx, nums[j])
            
            if point:
                if nums[i] < nums[i + length - 1]:
                    return False
            
            minn = maxx
        
        return True
    
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            if self.check(nums, k):
                ans += k
        
        return ans