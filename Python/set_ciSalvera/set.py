"1. Creazione di un Set",
    "- Set Vuoto: Un set vuoto può essere creato usando la funzione set().",
    "  Esempio: "
    my_set = set()
    "- Set con Elementi: Puoi creare un set direttamente con elementi passandoli all'interno di parentesi graffe {}.",
    "  Esempio: my_set = {1, 2, 3, 4}",
    
    "2. Aggiungere Elementi",
    "- Puoi aggiungere elementi a un set usando il"
    metodo add().
    "  Esempio:" 
    my_set.add(4)  # my_set diventa {1, 2, 3, 4}",
    "- Puoi anche aggiungere più elementi usando update(), che accetta un iterabile come input.",
    "  Esempio:" 
    my_set.update([5, 6])  # my_set diventa {1, 2, 3, 4, 5, 6}",
    
    "3. Rimuovere Elementi",
    "- remove(): Rimuove un elemento specifico. Genera un errore (KeyError) se l'elemento non è presente.",
    "  Esempio:" 
    my_set.remove(3)  # my_set diventa {1, 2, 4, 5, 6}",
    "- discard(): Simile a remove(), ma non genera un errore se l'elemento non è presente.",
    "  Esempio: "
    my_set.discard(10)  # Nessun errore, anche se 10 non è nel set",
    "- pop(): Rimuove e restituisce un elemento arbitrario dal set.",
    "  Esempio:" 
    popped_element = my_set.pop()  # Rimuove un elemento casuale",
    "- clear(): Rimuove tutti gli elementi dal set.",
    "  Esempio: "
    my_set.clear()  # my_set diventa set()",
    
    "4. Operazioni su Set",
    "- Unione (union o |): Restituisce un nuovo set che è l'unione di due set.",
    "  Esempio:" 
    union_set = set1.union(set2)  # {1, 2, 3, 4, 5}",
    "- Intersezione (intersection o &): Restituisce un nuovo set con gli elementi comuni a entrambi i set.",
    "  Esempio:" 
    intersection_set = set1.intersection(set2)  # {3}",
    "- Differenza (difference o -): Restituisce un nuovo set con gli elementi presenti solo nel primo set.",
    "  Esempio:" 
    difference_set = set1.difference(set2)  # {1, 2}",
    "- Differenza Simmetrica (symmetric_difference o ^): Restituisce un nuovo set con gli elementi presenti in uno dei due set, ma non in entrambi.",
    "  Esempio: "
    symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}",
    
    "5. Metodi di Confronto",
    "- Subset (<= o issubset()): Controlla se un set è un sottoinsieme di un altro.",
    "  Esempio:"
    is_subset = set1 <= set2  # True",
    "- Superset (>= o issuperset()): Controlla se un set è un sovrainsieme di un altro.",
    "  Esempio: "
    is_superset = set2 >= set1  # True",
    "- Disjoint (isdisjoint()): Controlla se due set non hanno elementi in comune.",
    "  Esempio:" 
    are_disjoint = set1.isdisjoint(set3)  # True",
    
    "6. Set Immutabili",
    "- Esiste una variante immutabile dei set chiamata frozenset. Una volta creato, non può essere modificato (simile a una tupla).",
    "  Esempio:" 
    frozen_set = frozenset([1, 2, 3])
    
    "7. Altri Metodi Utili",
    "- len(): Restituisce il numero di elementi in un set.",
    "  Esempio: set_length = len(my_set)",
    "- in: Controlla se un elemento è presente in un set.",
    "  Esempio: exists = 2 in my_set  # True"
]