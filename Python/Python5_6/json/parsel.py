def Serializza(myLista)->str:
    myString=str(myLista)
    return myString

def Deserializza(myString)->list:
    myLista=list(myString)
    return  myLista

myString="['mario', 'gigi', 'franco']"
myLista=['mario','gigi','franco']

sOut = Serializza(myLista)
print(type(sOut))
if sOut == myString:
    print("Procedura corretta")
else:
    print("Non corretta")

lOut= Deserializza(myLista)
if lOut == myLista:
    print("Procedura corretta")
else:
    print("Non corretta")  