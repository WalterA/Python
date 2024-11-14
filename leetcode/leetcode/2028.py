class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        somma_tot= len(rolls) * (n+mean)
        somma_rolls=sum(rolls)
        somma_mancante= somma_tot - somma_rolls
        if n <= somma_mancante <= somma_rolls:
            return [somma_mancante/n,somma_rolls/n]
        else:
            return []