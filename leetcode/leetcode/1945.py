class Solution:
    def getLucky(self, s: str, k: int) -> int:
            
        # Convert each letter to its corresponding number
        numbers = [str(ord(char) - ord('a') + 1) for char in s.lower() if char.isalpha()]
        # Combine the numbers into a single large integer
        large_number = int(''.join(numbers))
        stringa=str(large_number)
        conta=1
        result=0
        
        temp=0
        for i in stringa:
            temp+=int(i)
        st= str(temp)
        while conta < k:
            for i in st:
                result+=int(i)
            copy=result
            st=str(copy)
            result=0
            conta+=1
        return int(st)
            
                
s = "dbvmfhnttvr"
k = 5
sol=Solution()
print(sol.getLucky(s,k))