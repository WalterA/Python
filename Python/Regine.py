nt= 4

matrice = [[0]*nt]*nt
print(matrice)
indexr=0
indexc=0
regine= 4
print(matrice)
matrice[indexr][indexc] = 2
matrice[indexr][indexc+1]=1
print(matrice)
def controllor():
    for i in range(len(matrice[indexr])):
        if matrice[indexr][i] == 0:
            matrice[indexr][i]=1
        e
            
def Controllo(matrice,indexr,indexc,regine):
    while regine != 0:
        if matrice[indexr][indexc] == 0:
            matrice[indexr][indexc] = 1
            regine -= 1
            indexc
    return indexr,matrice

indexr,matrice = Controllo(matrice,indexr,indexc,regine)
print(matrice)


        
        