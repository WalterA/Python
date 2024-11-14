class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        lista = []
        maxy = max(candies)
        for i in candies:
            result = i + extraCandies
            if result >= maxy:
                lista.append(True)
            else:
                lista.append(False)
        return lista
    