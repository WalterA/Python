class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        copy=words.copy()
        for i in words:
            for j in i:
                if j in allowed:
                    continue
                else:
                    if i in copy:
                        copy.remove(i)
        return len(copy)

allowed = "fstqyienx"
words = ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]
sol=Solution()
print(sol.countConsistentStrings(allowed,words))