class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radiant = []
        dire = []
        
        # Popolare le liste con gli indici dei senatori
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # Simulare il processo di voto
        while radiant and dire:
            r = radiant.pop(0)
            d = dire.pop(0)
            
            # Il senatore con l'indice minore vince e può votare di nuovo
            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))
        
        # Determinare il vincitore
        return "Radiant" if radiant else "Dire"

# Esempio di utilizzo
sol= Solution()
senate = "RDD"
print(sol.predictPartyVictory(senate))  # Output: "Dire"

            
            
                
                
                
                
# senate = "DRDRR"#rdrd - drr-rd-r
# sol= Solution()
# print(sol.predictPartyVictory(senate))