class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    
            if count >= n:
                return True
        
        return count >= n

# Example usage:
solution = Solution()
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(solution.canPlaceFlowers(flowerbed1, n1))  # Output: True

flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(solution.canPlaceFlowers(flowerbed2, n2))  # Output: False

                
        
        
        
        
        
flow=[1]
n=1
sol=Solution()
print(sol.canPlaceFlowers(flow,n))
