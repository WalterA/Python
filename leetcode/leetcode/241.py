class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def helper(expression):
            if expression.isdigit():
                return [int(expression)]
            
            results = []
            for i, char in enumerate(expression):
                if char in "+-*":
                    left = helper(expression[:i])
                    right = helper(expression[i+1:])
                    
                    for l in left:
                        for r in right:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)
            
            return results
        
        return helper(expression)
e="2-1-1"

sol=Solution()
print(sol.diffWaysToCompute(e))