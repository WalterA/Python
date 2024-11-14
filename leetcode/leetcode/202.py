def isHappy(n: int) -> bool:
    temp=0
    while  range(100):
        if n >= 10:
            s=str(n)
            for i in s:
                temp += int(i)**2
            if temp == 1 or temp ==7:
                return True
            else:
                n=temp
                temp=0
        else:
            
            if n == 1 or n ==7:
                return True
            else:
                return False
    return False
        
        

n=2
isHappy(n)