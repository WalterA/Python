class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_operations = blocks[:k].count('W')
        current_operations = min_operations

        for i in range(1, len(blocks) - k + 1):

            if blocks[i - 1] == 'W':
                current_operations -= 1

            if blocks[i + k - 1] == 'W':
                current_operations += 1

            min_operations = min(min_operations, current_operations)

        return min_operations


blocks:str = "BWBWWBBBWWWWBBBWBBWBBWBBWWWWBBWB"
k:int  = 7
sol = Solution()
print(sol.minimumRecolors(blocks,k))
