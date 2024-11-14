class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        temp=[]
        arr.sort()
        indexpartenza=0
        indexdopo=1
        conta=0
        
        
        while indexdopo != len(arr):
            if arr[indexpartenza] == arr[indexdopo]:
                conta+=1
                indexpartenza+=1
                indexdopo+=1
            else:
                temp.append(conta)
                conta=0
                indexpartenza+=1
                indexdopo+=1
        temp.append(conta)
        if len(temp) == len(set(temp)):
            return True
        else:
            return False
        
        
arr = [-4,3,3]
sol=Solution()
print(sol.uniqueOccurrences(arr))

