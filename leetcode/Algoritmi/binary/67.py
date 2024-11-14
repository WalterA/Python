class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Converti le stringhe binarie in numeri interi
        num_a = int(a, 2)
        num_b = int(b, 2)

        # Somma i numeri interi
        sum_ab = num_a + num_b

        # Converti la somma in una stringa binaria
        result = bin(sum_ab)[2:]

        return result  # Output: "100"
