import sys, json

"""
TRACCIA:
Dato il file json maths.json scrivere un programma che risponde alle seguenti domande:
quante domande ci sono nel questionario?
quante sono, in media, il numero di risposte possibili?
quante domande ci sono di matematica?
"""

#versione1 risposta multipla diretta
def stampa_diz(dData):
    maths=0
    questions=0
    options=[]
    with open(dData,'r') as f:
        data=json.load(f)
    for keys , values in data.items():
                if keys == "quiz":
                    for k,v in values.items():
                        for k1,v1 in v.items():
                            if k == "maths":
                                maths+=1
                            for k2,v2 in v1.items():
                                if k2 == "options":
                                    options.append((len(v2)))
                                if k2 == "question":
                                    questions+=1
    media=sum(options)//len(options)
    return f"Ci sono:{questions} domande, Sono presenti in maths:{maths} domande, ci sono in media: {media} risposte"
dData='ITSCloud-main/Python/Python5_6/json/quiz.json'
print(stampa_diz(dData))

#versione2 risposta singola
# def stampa_diz(dData,sRoot):
#     """
#     Modalità d'uso
#     1)quante domande ci sono nel questionario? "question"
#     2)quante sono, in media, il numero di risposte possibili? "options"
#     3)quante domande ci sono di matematica? "maths"
#     Cambiare sRoot in base alla domanda il valore è fra "" dopo la domanda.
#     Nel caso della domanda 2 togliere il commento da media
#     Nel return inserire il valore che si ricerca [question or media or maths]
#     Togliere il commento da print
#     """

#     maths=0
#     questions=0
#     options=[]
#     with open(dData,'r') as f:
#         data=json.load(f)
#     for keys , values in data.items():
#                 if sRoot:
#                     for k,v in values.items():
#                         for k1,v1 in v.items():
#                             if k == sRoot:
#                                 maths+=1
#                             for k2,v2 in v1.items():
#                                 if k2 == sRoot:
#                                     options.append((len(v2)))
#                                 if k2 == sRoot:
#                                     questions+=1
#                 else:
#                     return "sRoot è vuota"
#     #media=sum(options)//len(options)
#     return f"{sRoot=}{maths}"
dData='ITSCloud-main\Python\Python5_6\json\quiz.json'
sRoot="maths"
#print(stampa_diz(dData,sRoot))
