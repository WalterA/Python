class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def euclide(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        if str1 + str2 != str2 + str1:
            return ""
        brooo = euclide(len(str1), len(str2))
        return str1[:brooo]
        
        
"""class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        common_prefix = ""
        min_len = min(len(str1), len(str2)) # Find the length of the shorter string between str1 and str2
        
        # Find the common prefix between the two strings
        for e in range(min_len):
            if str1[e] == str2[e]:  # If characters match at the current index
                common_prefix += str1[e]  # Add to the common prefix
            else:
                break  # Stop if characters don't match
        
        # We iterate from the length of common_prefix down to 1 (from the longest possible prefix to the shortest).
        for i in range(len(common_prefix), 0, -1): 
            candidate = common_prefix[:i]  # Extract the prefix of length i from common_prefix
            # We use replace to remove all occurrences of candidate from both str1 and str2. 
            # If the resulting strings are empty, it means candidate is a valid divisor for both strings.
            if str1.replace(candidate, "") == "" and str2.replace(candidate, "") == "":
                return candidate  # If true, return candidate as it is the longest common divisor
        
        # If no valid prefix found that can divide both str1 and str2, return an empty string
        return """""
    
str1 = "ABCABC"
str2 = "ABC"     
sol = Solution()
print(sol.gcdOfStrings(str1,str2))                       