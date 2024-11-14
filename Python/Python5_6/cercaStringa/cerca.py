import os

import PyPDF2
def CercaParola(file, sStringDaCercare):
    file=file.lower()
    sStringDaCercare=sStringDaCercare.lower()
    k=file.find(sStringDaCercare)
    if k >=0 :
        return True
    else: 
        return False
def cercaparoladentro(percorso,sStringDaCercare):
    bRet = False
    sfn, sfe =os.path.splitext(percorso)
    if (sfe.lower()==".txt"):
        bRet= cercainTxt(percorso,sStringDaCercare)
    if (sfe.lower()==".pdf"):
        bRet= cercapdf(percorso,sStringDaCercare)
    # if (sfe.lower()==".docx"):
    #     bRet= cercainDocx(percorso,sStringDaCercare)
    return bRet    
        
def cercainTxt(percorso,sStringDaCercare):
    with open(percorso,"r") as file1:
        sline=file1.readline()
        while len(sline)>0:
            iRet=sline.lower().find(sStringDaCercare.lower())
            if (iRet >=0):
                return True
            sline=file1.readline()
            print("riga letta:"+sline)
    return False

def cercapdf(percorsopippoplutoepaperino,sStringDaCercare):
    print("Richiamato per pdf")
    iRet=0
    object = PyPDF2.PdfReader(percorsopippoplutoepaperino)
    numpag=len(object.pages)
    print("pagine " + str(numpag))
    for i in range(0,numpag):
        pageobj=object.pages[i]
        text= pageobj.extract_text()
        iRet = text.lower().find(sStringDaCercare.lower())
        if iRet >=0:
            return True
        return False

sRoot=input('Inserisci la root directory:')
sStringDaCercare=input('inserisci la stringa da cercare:')
sOutDir=input('inserisci la dir di output:')
bRet = False
for root , dirs, files in os.walk(sRoot):
    # print(f"Nella directory {root} ci sono {len(dirs)} sottodirectory{len(files)}")
    #sToPrint="Dir corrente {0} contenente {1} sudbir e {2} files".format(root,len(dirs),len(files))
    #print(sToPrint)
    for file in files:
        print(f"devo cercare {sStringDaCercare} in {file}")
        bRet = CercaParola(file,sStringDaCercare)
        if (bRet==True):
            print("Trovato1:" + file)
        else:
            percorso = os.path.join(root,file)
            bRet= cercaparoladentro(percorso,sStringDaCercare)
            if (bRet==True):
                print("Trovato2:" +file)
            
            