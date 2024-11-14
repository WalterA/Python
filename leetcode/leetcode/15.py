# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         s = set(nums)
#         l= list(s)
#         temp=[]
#         lista=[]
#         numero_unico= l[-1]
#         inizio= 0
#         fine= len(l)
#         copy=temp.copy()
#         temp.append(numero_unico)
#         if len(nums)== 6:
#             while inizio != fine:
#                 if inizio == fine:
#                     return lista
#                 else:
#                     if len(temp) < 3:
#                         temp.append(l[inizio])
#                         inizio += 1
#                     else:
#                         summa = sum(temp)
#                         if summa == 0:
#                             copy=temp.copy()
#                             lista.append(copy)
#                             temp.clear()
#                             temp.append(numero_unico)
#                             inizio -= 1
#                         else:
#                             inizio -= 1
#                             temp.clear()
#                             temp.append(numero_unico)
#         else:
#             summa = sum(nums)
#             if summa == 0:
#                 return [nums]
#             else:
#                 []
                   
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

                
            
        
            
            
x= [-1,0,1,2,-1,-4]
sol =Solution()
print(sol.threeSum(x))
        