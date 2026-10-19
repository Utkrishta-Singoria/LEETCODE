# class Solution:
#     def scoreOfParentheses(self, s: str) -> int:
#         score=0
#         temp=0
#         stack=[]
#         x=0
#         for i in s:
#             if i == "(":
#                 stack.append(i)
#                 score += temp
#                 temp = 0
#                 x = 0
#             else:
#                 stack.pop()
#                 if x == 0 :
#                     temp += 1
#                     x += 1
#                 else:
#                     temp *= 2
#                     x += 1
#         return score
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                inside = stack.pop()

                if inside == 0:
                    stack.append(stack.pop() + 1)
                else:
                    stack.append(stack.pop() + 2 * inside)
        return stack.pop()