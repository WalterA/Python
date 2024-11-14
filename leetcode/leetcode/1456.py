
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Insieme delle vocali
        vocali = {'a', 'e', 'i', 'o', 'u'}
        
        # Conta le vocali nella prima finestra di lunghezza k
        max_vocali = sum(1 for i in range(k) if s[i] in vocali)
        # max_vocali = 0
        # for i in range(k):
        #     if s[i] in vocali:
        #         max_vocali += 1

        current_vocali = max_vocali
        
        # Scorri la stringa utilizzando la tecnica della finestra scorrevole
        for i in range(k, len(s)):
            if s[i] in vocali:
                current_vocali += 1
            if s[i - k] in vocali:
                current_vocali -= 1
            max_vocali = max(max_vocali, current_vocali)
        
        return max_vocali
    """class Solution:
    DAVIDE
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiouAEIOU"
        current_counter = 0
        max_counter = 0
        
        # Conta le vocali nella prima finestra di lunghezza k
        for i in range(k):
            if s[i] in vowels:
                current_counter += 1
        
        max_counter = current_counter
        
        # Scorri attraverso la stringa mantenendo una finestra di lunghezza k
        for i in range(k, len(s)):
            # Aggiungi la nuova lettera (fine della finestra)
            if s[i] in vowels:
                current_counter += 1
            # Rimuovi la lettera che esce dalla finestra
            if s[i - k] in vowels:
                current_counter -= 1
            
            # Aggiorna il massimo delle vocali trovate
            max_counter = max(max_counter, current_counter)
        
        return max_counter"""

# Esempio di utilizzo
s = "abciiidef"
k = 3
soluzione = Solution()
print(soluzione.maxVowels(s, k))  # Output: 3

