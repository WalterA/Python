class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        dispari=1
        while num !=0:
            num -=dispari
            if num < 0:
                return False
            dispari+=2
        return True
    
num=16
sol=Solution()
print(sol.isPerfectSquare(num))
