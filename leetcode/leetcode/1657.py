class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # Controlla se i set di caratteri sono uguali
        if set(word1) != set(word2):
            return False
        
        # Conta le frequenze dei caratteri
        frequenze_word1 = []
        for carattere in set(word1):
            frequenze_word1.append(word1.count(carattere))
        frequenze_word1.sort()
        """
        freq1 = sorted([word1.count(char) for char in set(word1)])
        freq2 = sorted([word2.count(char) for char in set(word2)])"""
        # Conta le frequenze dei caratteri in word2
        frequenze_word2 = []
        for carattere in set(word2):
            frequenze_word2.append(word2.count(carattere))
        frequenze_word2.sort()
        # Controlla se le frequenze sono uguali
        return frequenze_word1 == frequenze_word2

        """
        f=set(word1)
        r=set(word2)
        print(f,r)
        sa=f-r
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        if sa:
            return False
        else:
            return True"""
                
                
word1 = "a"
word2 = "aa"
sol=Solution()
print(sol.closeStrings(word1, word2))