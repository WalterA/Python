"""Given a signed 32-bit integer , return with its digits
reversed. If reversing causes the value to go outside the signed 32-bit
integer range , then return .xxx[-231, 231 - 1]0

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""
class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        z = list(y)
        jnstr = "".join(z)
        rev = jnstr[::-1]
        if x < 0:
            rev = "-" + rev[:-1]
        if int(rev) > 2**31 - 1 or int(rev) < -2**31:
            return 0
        return int(rev)
x = 901000
sol = Solution()
print(sol.reverse(x))