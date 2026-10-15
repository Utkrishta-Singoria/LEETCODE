class Solution:
    def isValid(self, s: str) -> bool:
        # bracket_map={")":"(", "}":"{","]":"["}
        # stack=[]
        # for i in s :
        #     if i in bracket_map:
        #         top_element = stack.pop() if stack else "#"
        #         if bracket_map[i] != top_element:
        #             return False
        #     else:
        #         stack.append(i)
        # return not stack
        stack=[]
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            else:
                if stack:
                    top_element = stack.pop()
                else:
                    return False
                if (top_element == "(") and (i != ")"):
                   return False 
                elif (top_element == "{") and (i != "}"):
                    return False
                elif (top_element == "[") and (i != "]"):
                    return False
        return not stack
                

                    