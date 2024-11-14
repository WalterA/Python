class Solution:
    def romanToInt(self, s: str) -> int:
        
        val = [
        900 ,400,90,40, 9,4,
        1000,500,
        100, 50,
        10, 5,
        1
        ]
        syb = [
            "CM" ,"CD","XC","XL","IX","IV",
            "M","D",
            "C","L",
            "X","V",
            "I"
        ]
        j=0
        i=0
        num = 0
        copy = ""
        copias= s
        while copias != "":
            j=0
            for _ in range(len(syb)):
                if syb[j] in copias:
                        copias=copias.replace(syb[j],"",1)
                        copy+= syb[j]
                        num += val[j]
                        j+=1
                        i+=1
                else:
                    j+=1
        return num
        
s ="MCMXCIV"
sol=Solution() 
print(sol.romanToInt(s))           