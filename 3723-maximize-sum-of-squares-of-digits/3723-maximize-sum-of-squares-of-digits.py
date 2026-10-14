# class Solution:
#     def maxSumOfSquares(self, num: int, sum: int) -> str:
#         low_range= 10**(num-1)
#         high_range = (10**num)
#         l1=[]
#         max_sum=0
#         ans=""
#         for i in range(low_range,high_range):
#             str1 = str(i)
#             var = 0
#             for i in str1:
#                 number = int(i)
#                 var += number
#             if var == sum:
#                 l1.append(str1)
#         for i in l1:
#             sum1 = 0
#             for j in i:
#                 number1 = int(j)
#                 sum1 += number1**2
#             if sum1 >= max_sum:
#                 max_sum = sum1
#                 ans = i
#         return ans
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num: return ""  # even all 9s can't reach the sum
        nines, rest = divmod(sum, 9)
        return ("9" * nines + str(rest) + "0" * num)[:num]  # 9s, then the rest, then zeros