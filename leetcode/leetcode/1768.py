class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        conta1= 0
        conta2= 0
        merged = ""
        length  = len(word1)
        length2 = len(word2)
        while length != conta1 or length2 != conta2:
            if length == length2:
                merged += word1[conta1]
                conta1 += 1
                merged += word2[conta2]
                conta2 += 1
            else:
                if length < length2:
                    while length != conta1:
                        merged += word1[conta1]
                        conta1 += 1
                        merged += word2[conta2]
                        conta2 += 1
                    while conta2 != length2:
                        merged += word2[conta2]
                        conta2 += 1
                else:
                    while length2 != conta2:
                        merged += word1[conta1]
                        conta1 += 1
                        merged += word2[conta2]
                        conta2 += 1
                    while conta1 != length:
                        merged += word1[conta1]
                        conta1 += 1
                    
        return merged
sol = Solution()
word1 = "ABCD"
word2 = "pq"
print(sol.mergeAlternately(word1,word2)) # Expected: "apbqcr"