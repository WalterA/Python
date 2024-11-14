class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        pos = {0: -1}
        state = 0
        max_length = 0
        
        # Vowel to bitmask mapping
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        for i, char in enumerate(s):
            if char in vowels:
                # Toggle the bit corresponding to the vowel
                state ^= vowels[char]
            
            if state in pos:
                # Calculate the length of the substring
                max_length = max(max_length, i - pos[state])
            else:
                # Store the first occurrence of the state
                pos[state] = i
        
        return max_length