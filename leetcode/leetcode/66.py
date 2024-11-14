
def plusOne(digits: list[int]) -> list[int]:
    temp=""
    lista=[]
    for i in digits:
        temp+=str(i)
    temp = int(temp)+1
    for i in str(temp):
        lista.append(int(i))
        
        
    print(lista)
    
digits = [1,2,3]
plusOne(digits)