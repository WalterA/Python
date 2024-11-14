class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """
        diz={}
        copy=sorted(arr.copy())
        lista= list(range(1,len(arr)+1))
        index=0
        while index != len(copy):
            if copy[index] in diz:
                copy.remove(copy[index])
            else:
                diz[copy[index]]=lista[index]
                index+=1
        for k,v in diz.items():
            while  k in arr:
                if k in arr:
                    arr[arr.index(k)]=str(v)
        arr=[int(i) for i in arr]
        return arr
        """
        """
        copy=sorted(list(set(arr.copy())))
        index=0
        if not arr:
            return []
        while arr[index] in copy:
                var=copy[copy.index(arr[index])]
                if  copy.index(var) ==0:
                    arr[arr.index(var)]=str((copy.index(var))+1)
                else:
                    arr[arr.index(var)]=str((copy.index(var))+1)
                
                if index == len(arr)-1:
                    break
                else:
                    index+=1
        arr=[int(i) for i in arr]
        return arr
        """
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        value_to_rank = {}  # Dictionary to store value-to-rank mapping
        sorted_unique_numbers = sorted(list(set(arr)))  # Remove duplicates and sort unique elements
        
        # Assign ranks to sorted unique elements
        for index in range(len(sorted_unique_numbers)): 
            value_to_rank[sorted_unique_numbers[index]] = index + 1
          
        # Replace each element in the original array with its rank
        for index in range(len(arr)): 
            arr[index] = value_to_rank[arr[index]]
        
        return arr  # Return the updated array
#[5,3,4,2,8,6,7,1,3]
arr =[37,12,28,9,100,56,80,5,12]
sol = Solution()
print(sol.arrayRankTransform(arr))