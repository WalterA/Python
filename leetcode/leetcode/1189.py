class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        diz={}
        x="balloon"
        for i in text:
            if i in x:
                if i in diz:
                    diz[i]+=1
                else:
                    diz[i]=1
             
        chiavi_necessarie = ["b", "a", "l", "o", "n"]
        tutte_presenti = True
        for chiave in chiavi_necessarie:
            if chiave not in diz:
                tutte_presenti = False
                break
        
        if tutte_presenti:
            
            diz['l'] //= 2
            diz['o'] //= 2
            
            
            min_occorrenze = diz['b']
            for chiave in chiavi_necessarie:
                if diz[chiave] < min_occorrenze:
                    min_occorrenze = diz[chiave]
            
            return min_occorrenze
        else:
            return 0
        
x="nlaebolko"
sol=Solution()
print(sol.maxNumberOfBalloons(x))
