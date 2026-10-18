class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        str1=str(x)
        if str1 == str1[::-1]:
            return True
        else:
            return False
        # for i in range(0,(len(str1))//2):
        #     if str1[i] != str1[(-i-1)]:
        #         return False
        # return True       