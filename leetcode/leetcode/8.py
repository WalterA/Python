"""Implement the function, which converts a string to a 32-bit signed integer.myAtoi(string s)

The algorithm for is as follows:myAtoi(string s)

Whitespace: Ignore any leading whitespace ()." "
Signedness: Determine the sign by checking if the next character is or , assuming positivity is neither present.'-''+'
Conversion: Read the integer by skipping leading zeros 
until a non-digit character is encountered or the end 
of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed 
integer range , then round the integer to remain in the range.
Specifically, integers less than should be rounded to , 7
and integers greater than should be rounded to .[-231, 231 - 1]-231-231231 - 1231 - 1
Return the integer as the final result."""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:  
            return 0
        p: list = list(s)
        lista = []
        if p[0] == "-":
            lista.append("-")
            p.pop(0)
        elif p[0] == "+":
            p.pop(0)
    			   			
        for e in p:
            if e in "1234567890":
                lista.append(e)
            else:
                break
            
        if len(lista) == 0:
            return 0
        elif len(lista) == 1 and lista[0] == "-":
            return 0	
        k = int("".join(lista))

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if k < INT_MIN:
            return INT_MIN
        if k > INT_MAX:
            return INT_MAX

        return k