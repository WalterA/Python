class Solution:
    def findComplement(self, num: int) -> int:
        binario = bin(num).replace("0b", "")
        complemento = ""
        
        for char in binario:
            if char == "1":
                complemento += "0"
            else:
                complemento += "1"
        
        intero = int(complemento, 2)
        return intero

# Esempio di utilizzo:
sol = Solution()
print(sol.findComplement(5))  # Output: 2
