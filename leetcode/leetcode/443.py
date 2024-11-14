class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        length = len(chars)
        
        while read < length:
            char = chars[read]
            count = 0
            
            while read < length and chars[read] == char:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
chars = ["a","a","a","b","c","c","d","d","d","d"]
sol = Solution()
print(sol.compress(chars))