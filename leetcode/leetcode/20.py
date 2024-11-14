class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack

# Example usage:
sol = Solution()
print(sol.isValid("()"))      # Output: true
print(sol.isValid("()[]{}"))  # Output: true
print(sol.isValid("(]"))      # Output: false


s ="()"
sol = Solution()
print(sol.isValid(s))
