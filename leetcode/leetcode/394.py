from typing import List
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ''
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()  # Rimuove '['
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * substr)
        return ''.join(stack)
                

s = "3[a2[c]]"
sol = Solution()
print(sol.decodeString(s))
