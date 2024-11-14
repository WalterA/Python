
def lengthOfLastWord(s: str):
    divisa = s.split()
    if divisa:
        return len(divisa[-1])
    else:
        return 0

s = "Hello World"
print(lengthOfLastWord(s))