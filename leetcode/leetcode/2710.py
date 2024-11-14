class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if '0' in num:
            x= num.replace('0','')
            return self.removeTrailingZeros(x)
        return x